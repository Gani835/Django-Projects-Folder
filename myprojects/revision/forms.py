from django import forms
from django.contrib.auth.forms import UserCreationForm
#from myprojects.DBoperations.models import Employee
from django.contrib.auth.models import User
from .models import Employee, products,product_detailes

'''
class EmpForm(forms.Form):
    empno=forms.IntegerField()
    empname=forms.CharField(max_length=20)
    empsalary=forms.IntegerField() '''
    
# Without using forms automatically render the forms. . .

class EmpForm(forms.ModelForm):
    class Meta: # Inner Class (Grouping the attributes in the class)
        model=Employee
        fields='__all__' # or fields=['empno','empname','empsalary']
        

class ImageExp(forms.ModelForm):
    class Meta:
        model=products
        fields='__all__'
        
class prodInfo(forms.ModelForm):
    class Meta:
        model=product_detailes
        fields='__all__'
        
