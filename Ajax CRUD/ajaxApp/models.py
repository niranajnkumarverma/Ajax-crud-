from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField

class UserProfile(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.Name





