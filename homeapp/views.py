from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    user = User.objects.exclude(id=request.user.id)
    return render(request,'homeapp/home.html',{'users':user})


def people(request):
    return render(request,'homeapp/people.html')

def bucket(request):
    return render(request,'homeapp/bucket.html')