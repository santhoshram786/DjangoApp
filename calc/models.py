from django.db import models

# Create your models here.

class Credentials(models.Model):

    userName = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
