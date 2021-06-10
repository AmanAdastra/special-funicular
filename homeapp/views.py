from django.shortcuts import render
from django.contrib.auth.models import User
from homeapp.forms import BucketForm
from homeapp.models import Bucket
from django.contrib.auth.decorators import login_required
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
            fm.save()
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