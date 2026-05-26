from enum import auto

from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField()
    content = models.TextField()
    Updated_on = models.DateTimeField(auto_now=True)
