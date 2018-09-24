# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    body = models.TextField()
    timestamp = models.DateField()
    category = models.ForeignKey(Category, default = "")
    tags = models.ManyToManyField(Tag, blank = True)

    def __str__(self):
        return self.title


