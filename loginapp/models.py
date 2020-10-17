from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=30) 
    email = models.EmailField(max_length=50) 
    password = models.CharField(max_length=32) 
    repassword = models.CharField(max_length=32) 
    mobilenumber = models.CharField(max_length=12)
