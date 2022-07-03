from distutils.text_file import TextFile
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.username