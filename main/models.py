from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    is_done = models.BooleanField(default = False)
    is_favorites = models.BooleanField(default = False)
   
class BookModel(models.Model):
    title = models.CharField(max_length=50)
    subtititle = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField(max_length=50)
    genre = models.CharField(max_length = 250)
    author = models.CharField(max_length = 300)
    year = models.DateTimeField()
    date = models.DateTimeField( )

    