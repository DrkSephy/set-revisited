from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name

    def __unicode__(self):
        return str(self.price)

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    account = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name

    def __unicode__(self):
        return str(self.account)
