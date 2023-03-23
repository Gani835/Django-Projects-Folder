from django.shortcuts import render 
from django.http import HttpResponse
from django.db import connection
from . models import Family,Employeeinfo
from .forms import EmpForm
# Create your views here.

def project(request):
    if request.method=='POST':
        uname=request.POST['name']
        uphone=request.POST['phone']
        info=project(YourName=uname,YourNumber=uphone)
        info.save()
        return HttpResponse('Detailes are Saved in DataBase')
    return render(request,'welcome.html')
    #return HttpResponse('Welcome To Mini Project')
    
# Family Form By using HTML input tags. . . .
    
def insfamilyinfo(request):
    if request.method=='POST':
        fathname=request.POST['fname']
        mothname=request.POST['mname']
        famdetailes=Family(Fathername=fathname,Mothername=mothname)
        famdetailes.save()
        return HttpResponse("Detailes are saved successfully. . . ")
    return render(request,'familyinfo.html')

# Fetching the Family Data. . . .

def fetchfamily(request):
    context={}
    if request.method=='POST':
        famid=request.POST['id']
        cur=connection.cursor()
        cur.execute('select * from ganeshdb1.miniproject_Family where id=%s',(famid,))
        data=cur.fetchall()
        context['faminfo']=data
    return render(request,'fetchfamilyinfo.html',context)
    #return HttpResponse('Family Data Retrived Successfully. . . .')
    
# EmpForm Without using HTML input Tags. . .. 

def empinfo(request):
    context={}
    context['empform']=EmpForm()
    if request.method=='POST':
        data=EmpForm(request.POST)
        
        if data.is_valid():
            eno=data.cleaned_data['employeeid']
            ename=data.cleaned_data['employeename']
            esalary=data.cleaned_data['employeesalary']
                       
            empobj=Employeeinfo(employeeid=eno,employeename=ename,employeesalary=esalary)
            empobj.save()
            return HttpResponse('Data Saved Successfully. . . .')
    return render(request,'empinfo.html',context)