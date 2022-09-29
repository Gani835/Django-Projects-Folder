from cgi import print_form
from contextlib import _RedirectStream
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from DBoperations.models import Employee
from django.db.models import Count,Sum,Max,Min
from .forms import EmpForm,ImageExp,prodInfo
from . models import Employee,products,Student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm

# Class Based View. . . . .
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.views.generic import TemplateView

# REVISION OF ORM. . . .

@login_required(login_url='login')

def Revision(request):
    
    # To return all Employees Detailes. . . .
    
    '''data=Employee.objects.all()
    print(data)
    
    for rec in data:
        print(rec.Employee_Name,rec.Employee_Salary)
    
    # To return Employee Name starts with a perticular letter. . . .
    
    data=Employee.objects.filter(Employee_Name__startswith='P')
    print(data)
    
    # To return Employee Name which contains perticular letter. . .
    
    data=Employee.objects.filter(Employee_Name__icontains='a')
    print(data)
    
    # To return Employee Name Whose salary greater than some amount. . . .
    
    data=Employee.objects.filter(Employee_Salary__gt=75000)
    print(data)
    
    # To return the count of Employees,Sum of Employees Salary,Maximum Salary and Minimum Salary,etc. . . .
    
    cnt=Employee.objects.aggregate(Count('Employee_Name'))
    print(cnt)
    
    data=Employee.objects.aggregate(Sum('Employee_Salary'))
    print(data)
    
    data=Employee.objects.aggregate(Max('Employee_Salary'))
    print(data)
    
    data=Employee.objects.aggregate(Min('Employee_Salary'))
    print(data)
    
    # To return Employee Names in Ascending and Descending order. . . .
    
    data=Employee.objects.all().order_by('Employee_Name')
    print(data)
    
    data=Employee.objects.all().order_by('-Employee_Name')
    print(data)
    
    # To return the groupby data of deptno, Count of Employee_Name,Sum of Employee_Salary. . . .
    
    data=Employee.objects.values('dept_no').annotate(Count('Employee_Name'))
    print(data)
    
    data=Employee.objects.values('dept_no').annotate(Sum('Employee_Salary'))
    print(data)
    
    return HttpResponse('I am revision app') 
    '''
    context={}
    context['empform']=EmpForm()
    
    if request.method=='POST':
        data=EmpForm(request.POST)
        
        if data.is_valid():
            '''eno=data.cleaned_data['empno']
            ename=data.cleaned_data['empname']
            esalary=data.cleaned_data['empsalary']
            
            empinfo=Employee(empno=eno,empname=ename,empsalary=esalary)
            empinfo.save()'''
            data.save()
            
            return HttpResponse('Data Saved Successfully')
        
    return render(request,'revision.html',context)

# AUTHENTICATION . . . . .

def userLogin(request):
    context={}
    
    if request.method =='POST':
        uname=request.POST['uname']
        upwd=request.POST['pwd']
        validUser=authenticate(username=uname,password=upwd)
        
        if validUser is not None:
            obj=EmpForm()
            context['empform'] = obj
            if request.user.is_authenticated:
                return render(request,'revision.html',context)
            else:
                login(request,validUser)
                return render(request,'revision.html',context)
        else:
            return HttpResponse('You are not a Valid User')
    
    return render(request,'login.html')

def userLogout(request):
    logout(request)
    return render(request,'login.html')

def createUser(request):
    context={}
    obj=UserCreationForm()
    context['signupform']=obj
    if request.method=='POST':
        newUser=UserCreationForm(request.POST)
        if newUser.is_valid():
            newUser.save()
            return redirect('login')
        else:
            print(newUser.errors)
            return redirect('signup')
            
    return render(request,'signup.html',context)

@user_passes_test(lambda user:user.is_staff,login_url='login')
def impFunction(request):
    return HttpResponse('I am an Important Page. . . .')


def imageprocessing(request):
    context={}
    context['form']=ImageExp()
    if request.method=='POST':
        data=ImageExp(request.POST,request.FILES)
        
        if data.is_valid():
            data.save()
            return HttpResponse('Data Saved Successfully')
        else:
            print(data.errors)
            return HttpResponse('Data is not Saved')

    return render(request,'image.html',context)

def productpage(request):
    context={}
    data=products.objects.all()
    context['info']=data
    return render(request,'productspage.html',context)

# Dynamic URL Creation . . .. . 

def dynurl(request,value):
    context={}
    #return HttpResponse(f'I have got {value} value')
    data=products.objects.filter(prodId=value)
    context['info']=data
    return render (request,'prodinfo.html',context)
    
    #return HttpResponse('I have got {value}')
    
def dynamicURL(request,value):
    context={}
    #return HttpResponse(f'I have got {value} value')
    data=products.objects.filter(prodId=value)
    context['info']=data
    return render (request,'productinfo.html',context)

def proddetailes(request):
    context={}
    context['form']=prodInfo()
    if request.method=='POST':
        data=prodInfo(request.POST)
        
        if data.is_valid():
            data.save()
            return HttpResponse("Data Stored Successfully. . . . .")
        else:
            return HttpResponse("Data Storing Was Failed. . . . .")
    
    return render(request,'proddetailes.html',context)

# Class Based Views Example . . . . .
# Create your views here.

class Myview(View):
    def get(self,request):
        #return HttpResponse('I am From Class Based Views. . . . ')
        return render(request,'classexp.html')
    
    def post(self,request):
        return HttpResponse(f"I have recieved {request.POST['name1']}")

# Some Important Class Based Generic Views. . . .

# 1) CreateView:-

class StudentForm(CreateView):
    model=Student
    fields='__all__'
    success_url='stdnt'
    
# 2) ListView or RetrieveView:-To view Multiple instances of a Table in DataBase.

class StudentList(ListView):
    model=Student
    
# 3) DetailView:- It displays one instance of a table in the DataBase.
#Django automatically assigns a "primary key" for each entry, and we need to 
# specify the <pk> in the request.

class StudentDetail(DetailView):
    model=Student
    
# 4) UpdateView:-To update the particular instance of the table from the database with some more details.
    
class StudentUpdate(UpdateView):
    model=Student
    fields='__all__'
    
# 5) DeleteView:- To delete the instance of a table in the DataBase.

class StudentDelete(DeleteView):
    model=Student
    success_url='/'
    
    
