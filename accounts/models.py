from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Moderator(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)