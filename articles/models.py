#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify


# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(allow_unicode=True,max_length=200,unique=True,blank=True,null=True)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(upload_to = 'media/pic_folder/', default = 'media/pic_folder/None/no-img.jpg')
    author=models.ForeignKey(User, default=None)


    


    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:200]