from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm,authenticate
from django.contrib.auth.models import User
from django import forms
from .models import Profile


# SignupForm

class UserSignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}))
    class Meta:
        model = User
        fields = ['username','email']
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','autocomplete':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
        
        
class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control ','autocomplete':'on','placeholder':'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','autocomplete':'on','placeholder':'Nickname'}))
    class Meta:
        model = User
        labels = {
            'username': 'Writer',
        }
        
class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['id','first_name','email','last_login']
        labels ={
            'last_login':'Last Active',
            'first_name': 'Name',
            'email':'Email'
        }
        widgets ={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_login':forms.DateTimeInput(attrs={'class':'form-control','readonly':'readonly'}),
            "email":forms.EmailInput(attrs={'class':'form-control'})
        }
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('interest','habit','want')
        widgets = {
            'interest':forms.Textarea(attrs={'class':'form-control textarea'}),
            'habit':forms.Textarea(attrs={'class':'form-control textarea'}),
            'want':forms.TextInput(attrs={'class':'form-control'}),
        }