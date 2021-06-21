from django.shortcuts import render
from django.contrib.auth.models import User
from homeapp.forms import BucketForm
from homeapp.models import Bucket
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from logsys.models import Profile
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"



def home(request):
    user = User.objects.exclude(id=request.user.id)
    return render(request,'homeapp/home.html',{'users':user})


def people(request):
    user = User.objects.all().order_by('last_login')
    # Pagination Stuff
    page = request.GET.get('page', 1)
    paginator = Paginator(user, 4)
    try:
        user = paginator.page(page)
    except EmptyPage:
        user = {}
    # End Pagination Stuff
    if is_ajax(request):
        return render(request, 'homeapp/persons.html', {'users': user})
    context = {
        'users':user
    }
    return render(request,'homeapp/people.html',context)


@login_required(login_url='/logsys/login/')
def bucket(request):
    if request.method=="POST":
        fm = BucketForm(request.POST,request.FILES)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.user = request.user
            instance.save()
            obj = Profile.objects.get(user=request.user)
            obj.rep+=10
            obj.save()
            return redirect("bucket")
        
    fm = BucketForm()
    stuff = Bucket.objects.all().order_by('-date')
    # Pagination Stuff
    page = request.GET.get('page', 1)
    paginator = Paginator(stuff, 4)
    try:
        stuff = paginator.page(page)
    except EmptyPage:
        stuff = {}
    # End Pagination Stuff
    if is_ajax(request):
        return render(request, 'homeapp/items.html', {'items': stuff})
    context = {
        'items':stuff,
        'form':fm,
    }
    return render(request,'homeapp/bucket.html',context)







# Function for deleting items of user

def bucketitemdel(request,id):
    try:
        obj = Bucket.objects.get(pk=id)
        obj.delete()
    except:
        messages.error('Try Again letter')
    return redirect("profile")