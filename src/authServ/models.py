import random
import uuid

from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    code = models.UUIDField(default=uuid.uuid4())
    detail = models.CharField(max_length=350)


class User(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNo = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    code = models.UUIDField(default=uuid.uuid4())
    dateOfBith = models.DateField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Client(models.Model):
    pIdCard1 = models.CharField(max_length=500)
    code = models.UUIDField(default=uuid.uuid4())
    pIdCard2 = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Customer(models.Model):
    pIdCard1 = models.CharField(max_length=500)
    code = models.UUIDField(default=uuid.uuid4())
    pIdCard2 = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Admin(models.Model):
    salary = models.FloatField(null=True, default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserAccount(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phoneNo = models.CharField(max_length=30)
    username = None
    identifiant = models.CharField(max_length=100, null=True)
    blocked = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    role = models.CharField(max_length=10)
    opt = models.CharField(max_length=6, blank=True, null=True)

    lastActivity = models.DateTimeField(null=True)
    lat = models.FloatField(null=True)
    lastIpAddress = models.CharField(max_length=19)
    lng = models.FloatField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []





