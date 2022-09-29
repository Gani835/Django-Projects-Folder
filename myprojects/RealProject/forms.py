from socket import fromshare
from django import forms
from .models import loginpage

class loginform(forms.ModelForm):
    model=loginpage
    fields='__all__'
