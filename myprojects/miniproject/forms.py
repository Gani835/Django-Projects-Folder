from django import forms
from . models import Employeeinfo

# Creating EmpForm by using Form class and without using HTML input Tags. .. . .

'''class EmpForm(forms.Form):
    employeeid=forms.IntegerField()
    employeename=forms.CharField(max_length=20)
    employeesalary=forms.IntegerField()'''
    
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employeeinfo
        fields='__all__'
        