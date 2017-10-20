from django.contrib import admin
from django.views.generic import list

from models import *
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','desc','created','user','category']
    list_filter = ['title']
    search_fields = ['title']
admin.site.register(Category)
admin.site.register(Post,PostModelAdmin)