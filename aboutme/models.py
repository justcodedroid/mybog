#coding=UTF-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=250)
    def __str__(self):
        return self.name.encode("UTF-8")

# 在什么时间什么地点学了什么东西
class Education(models.Model):
    start = models.DateField()
    end = models.DateField()
    address = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    user = models.ForeignKey(User)
#     在什么时间什么地点什么人以什么职务做了什么事情
class Exprience(models.Model):
    start = models.DateField()
    end = models.DateField()
    address = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User)

class ExprienceItem(models.Model):
    desc = models.CharField(max_length=250)
    exprience = models.ForeignKey(Exprience)

class Skill(models.Model):
    desc = models.CharField(max_length=100)
    user = models.ForeignKey(User)