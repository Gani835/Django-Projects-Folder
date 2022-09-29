from django.forms import ModelForm
from.models import Amazonproducts
from django import forms
#class productsform(ModelForm):
 #   class Meta:
  #      model=Amazonproducts
   #     fields='__all__'
   
class productsform(forms.Form):
    prodId=forms.IntegerField()
    prodname=forms.CharField(max_length=20)
    prodprice=forms.IntegerField()
    
    

    