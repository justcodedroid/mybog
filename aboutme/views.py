#coding=UTF-8
from django.shortcuts import render
from django.http.response import HttpResponse
from models import *
# Create your views here.
def index(request):
    user=User.objects.get(name='树先生')
    educations = user.education_set.all()
    expriences = user.exprience_set.all()
    skills = user.skill_set.all()
    context={}
    context['user']=user
    context['educations']=educations
    context['expriences']=expriences
    context['skills']=skills
    return render(request,'aboutme/about.html',context)