from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    is_done = models.BooleanField(default = False)
    is_favorites = models.BooleanField(default = False)
   
class Book(models.Model):
    title = models.CharField(max_length=50)
    subtititle = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    genre = models.CharField(max_length = 50)
    author = models.CharField(max_length = 150)
    year = models.DateField()
    is_favorites= models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
   

    