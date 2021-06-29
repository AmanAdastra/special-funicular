from django.shortcuts import render
from django.contrib.auth.models import User
from homeapp.forms import BucketForm, ArticleForm, ProjectForm
from homeapp.models import Bucket, Article, Project
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from logsys.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def home(request):
    user = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        fm = ProjectForm(request.POST, request.FILES)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.user = request.user
            instance.save()
            obj = Profile.objects.get(user=request.user)
            obj.rep += 10
            obj.save()
            return redirect("home")

    fm = ProjectForm()
    project = Project.objects.all().order_by("-date")
    # Pagination Stuff
    page = request.GET.get("page", 1)
    paginator = Paginator(project, 2)
    try:
        project = paginator.page(page)
    except EmptyPage:
        project = {}
    # End Pagination Stuff
    if is_ajax(request):
        return render(request, "homeapp/home/project.html", {"items": project})
    context = {
        "items": project,
        "form": fm,
        "activeness": "home",
        "users": user,
    }
    return render(request, "homeapp/home/home.html", context)


def people(request):
    user = User.objects.all().order_by("last_login")
    # Pagination Stuff
    page = request.GET.get("page", 1)
    paginator = Paginator(user, 4)
    try:
        user = paginator.page(page)
    except EmptyPage:
        user = {}
    # End Pagination Stuff
    if is_ajax(request):
        return render(request, "homeapp/people/persons.html", {"users": user})
    context = {
        "users": user,
        "activeness": "people",
    }
    return render(request, "homeapp/people/people.html", context)


@login_required(login_url="/logsys/login/")
def bucket(request):
    if request.method == "POST":
        fm = BucketForm(request.POST, request.FILES)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.user = request.user
            instance.save()
            obj = Profile.objects.get(user=request.user)
            obj.rep += 10
            obj.save()
            return redirect("bucket")

    fm = BucketForm()
    stuff = Bucket.objects.all().order_by("-date")
    # Pagination Stuff
    page = request.GET.get("page", 1)
    paginator = Paginator(stuff, 4)
    try:
        stuff = paginator.page(page)
    except EmptyPage:
        stuff = {}
    # End Pagination Stuff
    if is_ajax(request):
        return render(request, "homeapp/bucket/items.html", {"items": stuff})
    context = {
        "items": stuff,
        "form": fm,
        "activeness": "bucket",
    }
    return render(request, "homeapp/bucket/bucket.html", context)


# Function for deleting items of user


def bucketitemdel(request, id):
    try:
        obj = Bucket.objects.get(pk=id)
        obj.delete()
    except:
        messages.error("Try Again letter")
    return redirect("profile")


def articleitemdel(request, id):
    try:
        obj = Article.objects.get(pk=id)
        obj.delete()
    except:
        messages.error("Try Again letter")
    return redirect("profile")


# Funciton for globe


@login_required(login_url="/logsys/login/")
def globe(request):
    if request.method == "POST":
        fm = ArticleForm(request.POST, request.FILES)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.user = request.user
            instance.save()
            obj = Profile.objects.get(user=request.user)
            obj.rep += 10
            obj.save()
            return redirect("globe")

    fm = ArticleForm()
    stuff = Article.objects.all().order_by("-date")
    # Pagination Stuff
    page = request.GET.get("page", 1)
    paginator = Paginator(stuff, 3)
    try:
        stuff = paginator.page(page)
    except EmptyPage:
        stuff = {}
    # End Pagination Stuff
    if is_ajax(request):
        return render(request, "homeapp/globe/articles.html", {"articles": stuff})
    context = {"articles": stuff, "form": fm, "activeness": "globe"}
    return render(request, "homeapp/globe/globe.html", context)


# Show full article


def fullarticle(request, id):
    article = Article.objects.get(pk=id)
    if request.method == "POST":
        fm = ArticleForm(request.POST, request.FILES, instance=article)
        if fm.is_valid():
            fm.save()
            return redirect("/fullarticle/" + str(id))
    else:
        fm = ArticleForm(instance=article)
    return render(
        request,
        "homeapp/globe/fullarticle.html",
        {"article": article, "form": fm, "activeness": "article"},
    )
