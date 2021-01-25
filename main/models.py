from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    is_done = models.BooleanField(default = False)
    is_favorites = models.BooleanField(default = False)