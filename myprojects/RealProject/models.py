from django.db import models

# Create your models here.

class Signuppage(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Username=models.CharField(max_length=20,null=True)
    Password=models.CharField(max_length=20)
    PasswordAgain=models.CharField(max_length=20)
    
class loginpage(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    
class Mainpage(models.Model):
    Textarea=models.TextField(max_length=10000)