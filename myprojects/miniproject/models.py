from django.db import models

# Create your models here.

# Creatinf a Form By Using HTML input Tags. . .. 

class Family(models.Model):
    Fathername=models.CharField(max_length=20)
    Mothername=models.CharField(max_length=20)

    def __str__(self):
        return self.Fathername
    
    class Meta:
        verbose_name_plural='Families'
        

# Creating a Form by using ModelForm class. . . .

class Employeeinfo(models.Model):
    employeeid=models.IntegerField(primary_key=True)
    employeename=models.CharField(max_length=20)
    employeesalary=models.IntegerField()
    empaddress=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.employeename