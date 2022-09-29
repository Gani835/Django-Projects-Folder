from curses.ascii import HT
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .models import Signuppage
from . forms import loginform
from django.contrib.auth import authenticate,login
# Create your views here.

def realProject(request):
    if request.method=='POST':
        fstname=request.POST['fname']
        lstname=request.POST['lname']
        emailadd=request.POST['email']
        uname=request.POST['username']
        pwd=request.POST['pwd1']
        pwda=request.POST['pwd2']
        
        userdetailes=Signuppage(FirstName=fstname,LastName=lstname,Email=emailadd,Username=uname,Password=pwd,PasswordAgain=pwda)
        userdetailes.save()
        return render(request,'backpage.html')
    return render (request,'signuppage.html')
      
      
def loginpage(request):
    context={}
    
    if request.method=='POST':
        username=request.POST['uname']
        passwrd=request.POST['pwd']
        
        validuser=authenticate(Username=username,Password=passwrd)
        
        '''if validuser is not None:
            obj=loginform()
            context['loginform']=obj'''
        
        if request.user.is_authenticated:
            #return HttpResponse('You are a valid user')
            return render(request,'mainpage.html')
        else:
            login(request,validuser)
            return render(request,'loginpage.html')
        
    return render(request,'loginpage.html')

def mainpage(request):
    if request.method=='POST':
        textarea=request.POST['text']
        textarea.save()
        return render(request,'homee.html')
    
    
    