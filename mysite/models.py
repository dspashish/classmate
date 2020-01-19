
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ShowSubClass(models.Model):
    std = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    