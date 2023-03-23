from socket import fromshare
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from.models import another_model

class NewForm(forms.Form):
    class Meta:
        model=another_model
        fields='__all__'
    

def texteditor(request):
    if request.method=='POST':
        form=NewForm(request.POST)
        if form.is_valid():
            form.save()
    form=NewForm()
    return render(request,'texteditor.html',{'form':form})
