from django.urls import path, include
from .views import userlogin,userlogout,userprofile,usersignup,showprofile,UserViewSet,userpasschange
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("",UserViewSet,basename='userview')


urlpatterns = [
    path("login/",userlogin,name='login'),
    path("signup/",usersignup,name='signup'),
    path("profile/",userprofile,name='profile'),
    path("logout/",userlogout,name='logout'),
    path("uprofile/<int:id>",showprofile,name='uprofile'),
    
    # password reset paths
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='logsys/password_reset.html'),name='password_reset'),
    path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name='logsys/password_reset_done.html'),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='logsys/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='logsys/password_reset_complete.html'),name='password_reset_complete'),
    
    
    # For user api
    path("user/",include(router.urls)),
    path('passchange/',userpasschange,name='passchange'),
    
]