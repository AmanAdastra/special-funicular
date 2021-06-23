from django.urls import path
from homeapp import views
urlpatterns = [
    path("",views.home,name='home'),
    path("bucket/",views.bucket,name='bucket'),
    path("people/",views.people,name='people'),
    path("globe/",views.globe,name='globe'),
    path('fullarticle/<int:id>/',views.fullarticle,name='fullarticle'),
    path('delitem/<int:id>/',views.bucketitemdel,name='delitem'),
]