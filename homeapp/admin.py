from django.contrib import admin
from .models import Bucket
# Register your models here.

@admin.register(Bucket)
class AdminBucket(admin.ModelAdmin):
    list_display = ['id','image','notes','date']