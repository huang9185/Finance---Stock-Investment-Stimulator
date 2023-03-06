from django.db import models
from django.contrib.auth.models import User

class User(User):
    pass

class Watch(models.Model):
    user = models.IntegerField()
    quote = models.CharField(max_length=10) # stored in uppercase
    company = models.CharField(max_length=50) # uppercase
    first_created = models.DateTimeField(auto_now=False, auto_now_add=True)

class Purchase(models.Model):
    user = models.IntegerField()
    quote = models.CharField(max_length=10)
    first_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    number = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    label = models.CharField(max_length=50, default="bought")

class Sell(models.Model):
    user = models.IntegerField()
    quote = models.CharField(max_length=10)
    first_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    number = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    label = models.CharField(max_length=50, default="sold")

class Share(models.Model):
    user = models.IntegerField()
    quote = models.CharField(max_length=10)
    numberTotal = models.IntegerField()
    paidTotal = models.DecimalField(max_digits=15, decimal_places=2)
    earnedTotal = models.DecimalField(max_digits=15, decimal_places=2, default=0)