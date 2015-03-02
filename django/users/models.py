from django.db import models

class User(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=128)
x
