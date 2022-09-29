from django.db import models

# Create your models here.
   
class Family(models.Model):
    FatherName=models.CharField(max_length=20)
    MotherName=models.CharField(max_length=20)
    SonName=models.CharField(max_length=20)
    Daughter_1_Name=models.CharField(max_length=20)
    Daughter_2_Name=models.CharField(max_length=20)
    Village_Name=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.FatherName

# Taking Another model For Creating A New Table In DataBase:-

class Product_Detailes(models.Model):
    Product_Company=models.CharField(max_length=20)
    Cream_Base=models.CharField(max_length=20)
    Scrub_Base=models.CharField(max_length=20)
    Lotion_Base=models.CharField(max_length=20)
    Oil_Base=models.CharField(max_length=20)
    Gel_Base=models.CharField(max_length=20)
    Soap_Base=models.CharField(max_length=20)
    
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=20)

    def __str__(self):
        return self.deptname
    
class Employee(models.Model):
    Employee_Name=models.CharField(max_length=20)
    Employee_Salary=models.IntegerField() 
    Employee_Address=models.TextField(max_length=200,null=True)
    dept_no=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.Employee_Name
    
    class Meta:
        ordering=['Employee_Name'] # Ascending order of Names
        ordering=['Employee_Salary'] # Ascending order of Salaries
        