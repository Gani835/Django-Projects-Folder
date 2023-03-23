from django import forms
class formexp(forms.Form):
    Name=forms.CharField(max_length=10)
    Age=forms.IntegerField()    
