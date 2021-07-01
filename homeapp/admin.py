from django.contrib import admin
from .models import Bucket,Article,Project
# Register your models here.

@admin.register(Bucket)
class AdminBucket(admin.ModelAdmin):
    list_display = ['id','image','notes','date','user']

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ['id','image','notes','date','user']
    
    
@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['id','heading','image','theory','date','user']