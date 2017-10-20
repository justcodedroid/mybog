#coding=UTF-8
#新增了一行注释
#新增了个人简历
# 新增了归档
from django.shortcuts import render
from django.http.response import HttpResponse
from models import *
from  markdown import markdown
# Create your views here.
def index(request,pageNum=1):
    page = Post.getPage(pageNum)
    posts = page.object_list
    for post in posts:
        post.desc = markdown(post.desc)
    context={'posts':posts,'page':page}
    before = 4
    last = 5
    current = page.number
    if current>=before:
        start = current-before
        end = current+last
    else:
        start=0
        end=last+before
    page_range=list(page.paginator.page_range)[start:end]
    context['page_range']=page_range
    # page.has_previous()
    return render(request,'post/index.html',context)


def details(request,id):
    post = Post.objects.get(id=id)
    post.content=markdown(post.content)
    return render(request,'post/details.html',{'post':post})