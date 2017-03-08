from django.contrib.auth.models import User
from django.db import models


class Color(models.Model):
    staff = models.CharField(max_length=200)
    color = models.CharField(max_length=10)
