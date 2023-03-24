from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False, default="Item")
    details = models.CharField(max_length=500, null=False, default="Details")
    img_url = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=5, default=0.0, null=False)
    
# class Users(models.Model):

#     username = models.CharField(max_length=50, unique=True, null=False, default="username")
#     email = models.CharField(max_length=100, unique=True, null=False, default="email")
#     password = models.CharField(max_length=200, null=False, default="password")
