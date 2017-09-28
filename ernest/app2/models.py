# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TestUpload(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    brithday = models.DateTimeField()
    #代表這筆資料回傳值
    def __str__(self):
        return self.name