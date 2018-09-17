from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 150)
    discription = models.TextField()
    body = models.TextField()
    timestamp = models.DateField()
