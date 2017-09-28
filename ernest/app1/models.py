# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    q = models.Manager()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Profile(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    brithday = models.DateTimeField()
    #代表這筆資料回傳值
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    img_name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to='photoimg',null=False)
    def __str__(self):
        return self.img_name