from django.db import models
import django.contrib.auth.models


# Create your models here.
class Vacancy(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)

