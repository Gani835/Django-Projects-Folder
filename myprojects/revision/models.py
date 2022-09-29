from distutils.command.upload import upload
from django.db import models
#from django.db.models.signals import pre_save,post_save,post_delete

# Create your models here.

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=20)
    empsalary=models.IntegerField()
    empaddress=models.CharField(max_length=100,null=True)
    
# ABSTRACT INHERITANCE. . .  .

class Base(models.Model):
    empno=models.IntegerField(null=True)            
    empaddress=models.TextField(max_length=100)
    
# Note:- I dont want to create Base class as a Table thats why i'm creating Inner Meta class and take abstract is True. . . 
# Only Canteen Table was created in DataBase. . . .

    class Meta:
        abstract=True
    
class Canteen(Base):
    tiffin_menu=models.CharField(max_length=20)
    
# MULTI INHERITANCE. . . .
# Both Tcs and Transport Tables are created in Database. . .. 

class Tcs(models.Model):
    empno=models.IntegerField(null=True)            
    empname=models.CharField(max_length=10)
        
class Transport(Tcs):
    routes=models.CharField(max_length=20)
        
# PROXY INHERITANCE. . . . (MEANS DUPLICATE)
# Creating a Duplicate Table 

class products(models.Model):
    prodId=models.IntegerField(primary_key=True)
    prodname=models.CharField(max_length=20)
    prodimage=models.ImageField(null=True, blank=True, upload_to='media/')
    proddesc=models.TextField(max_length=100,null=True)
    prodprice=models.IntegerField(null=True)
    
    class Meta:
        verbose_name_plural='products'
        
    def __str__(self):
        return self.prodname
    
class product_detailes(models.Model):
    prodId=models.IntegerField(primary_key=True)
    prodname=models.CharField(max_length=20)
    proddesc=models.TextField(max_length=100,null=True)
    prodprice=models.IntegerField()
    prodimage=models.ImageField(null=True,blank=True,upload_to='media/')
    
    class Meta:
        verbose_name_plural='product_detailes'
        
    def __str__(self):
        return self.prodname
    
    
class Student(models.Model):
    StudentName=models.CharField(max_length=20)
    StudentAge=models.IntegerField()
    StudentAddress=models.CharField(max_length=20)
    
# Signals:-Whenever an action performed on a table, a signal will be sent. . . .

# Pre Signal:-( BLearning Club Youtube Channel )

'''def student_postsave(sender,instance,**kwargs):
    print('Post save signal hasbeen recieved')
    #print(kwargs)   # It gives an object
    #print(instance.StudentName,instance.StudentAddress) # to retrieve the detailes what we changed.
#Note:- Here receiver is the function sender is the model.
post_save.connect(student_postsave,sender=Student)
pre_save.connect(student_postsave,sender=Student)

# Post delete:-

def student_postdelete(sender,instance,**kwargs):
    print('Your post hasbeen deleted')

post_delete.connect(student_postdelete,sender=Student)


def student_postsave(sender,instance,created,*args,**kwargs):
    print('post save signal hasbeen recieved')
    print(created)'''