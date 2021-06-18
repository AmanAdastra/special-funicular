from django.shortcuts import render
from django.contrib.auth.models import User
from homeapp.forms import BucketForm
from homeapp.models import Bucket
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def home(request):
    user = User.objects.exclude(id=request.user.id)
    return render(request,'homeapp/home.html',{'users':user})


def people(request):
    return render(request,'homeapp/people.html')


@login_required(login_url='/logsys/login/')
def bucket(request):
    if request.method=="POST":
        fm = BucketForm(request.POST,request.FILES)
        if fm.is_valid():
            instance = fm.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("bucket")
    else:
        fm = BucketForm()
    stuff = Bucket.objects.all()
    context = {
        'items':stuff,
        'form':fm,
    }
    return render(request,'homeapp/bucket.html',context)

def people(request):
    return render(request,'homeapp/people.html')





# Function for deleting items of user

def bucketitemdel(request,id):
    try:
        obj = Bucket.objects.get(pk=id)
        obj.delete()
    except:
        messages.error('Try Again letter')
    return redirect("profile")