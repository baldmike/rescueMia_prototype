from __future__ import unicode_literals
from django.utils import timezone as django_tz
from django.db import models
 
class Dog(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    color = models.CharField(max_length = 20)
    size = models.CharField(max_length = 20)
    fixed = models.CharField(max_length = 3)
    vaccine = models.DateTimeField(default = django_tz.now)
    adopted = models.BooleanField(max_length = 3, default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
