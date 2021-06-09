from django.shortcuts import render
from .forms import UserSignupForm,UserLoginForm, UserProfileForm,ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


# User signup view

def usersignup(request):
    if request.method=="POST":
        fm = UserSignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("login")
    else:
        fm = UserSignupForm()
    return render(request,"logsys/signup.html",{"form":fm})



def userlogin(request):
    if request.method=="POST":
        fm = UserLoginForm(request  = request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect("home")
    else:
        fm = UserLoginForm()
    return render(request,"logsys/login.html",{'form':fm})



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

    return render(request,"logsys/profile.html",{'form':fm,'profile_form': profile_form})

@login_required(login_url='/logsys/login/')
def userlogout(request):
    logout(request)
    return redirect("home")



@login_required(login_url='/logsys/login/')
def showprofile(request,id=1):
    user = User.objects.get(pk=id)
    return render(request,"logsys/showprofile.html",{'user':user})