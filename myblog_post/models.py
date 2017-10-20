from __future__ import unicode_literals

from django.db import models
from aboutme.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return  u'%s'%self.name
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=520)
    content = models.TextField(blank=True)
    created = models.DateField()
    user = models.ForeignKey(User)
    category= models.ForeignKey(Category)
    @staticmethod
    def getPage(pageNum):
        from  django.core.paginator import  Paginator,InvalidPage,EmptyPage
        try:
            pageNum=int(pageNum)
        except:
            pageNum=1
        pageinator=Paginator(Post.objects.order_by('-created').all(),1)
        try:
            page = pageinator.page(pageNum)
        except InvalidPage,EmptyPage:
            page = pageinator.page(1)
        return  page