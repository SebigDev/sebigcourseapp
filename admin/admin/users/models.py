from django.db import models

class Address(models.Model):
    phone_number = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=10)
    street_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

class User(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email_address = models.EmailField(max_length=200, blank=True, unique=True)
    age = models.PositiveBigIntegerField()
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, related_name='address')
    date_registered = models.DateField(auto_now_add=True) 