from django.shortcuts import render
from .forms import UserSignupForm,UserLoginForm, UserProfileForm,ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from homeapp.models import Bucket
# Create your views here.


# User signup view

def usersignup(request):    
    if request.method=="POST":
        fm = UserSignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=fm.cleaned_data['username'],
                                    password=fm.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("profile")
        else:
            messages.error(request,"Please enter Credentials according to our policy")
    return redirect("login")
    



def userlogin(request):
    
    if request.user.is_authenticated:
        return redirect("profile")
    fm2= UserSignupForm(label_suffix='')
    if request.method=="POST":
        fm = UserLoginForm(request  = request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                return redirect("home")
    else:
        fm = UserLoginForm()
    return render(request,"logsys/login.html",{'form':fm,'form2':fm2})



@login_required(login_url='/logsys/login/')
def userprofile(request):
    if request.method=="POST":
        fm = UserProfileForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if fm.is_valid():
            fm.save()
            profile_form.save()
            messages.success(request,"Your Profile is Updated!")
    else: 
        fm = UserProfileForm(instance = request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    items = Bucket.objects.filter(user=request.user.id)
    context = {
        'form':fm,
        'profile_form': profile_form,
        'items':items,
        }

    return render(request,"logsys/profile.html",context)

@login_required(login_url='/logsys/login/')
def userlogout(request):
    logout(request)
    return redirect("home")



@login_required(login_url='/logsys/login/')
def showprofile(request,id=1):
    user = User.objects.get(pk=id)
    items = Bucket.objects.filter(user=user.id)
    context = {
        'user':user,
        'items':items
        }
    return render(request,"logsys/showprofile.html",context)






# API for user view
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
    
