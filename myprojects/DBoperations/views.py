from django.shortcuts import render,HttpResponse
from django.db import connection
from .models import Family, Product_Detailes,Employee


# Create your views here.

# To Fetch the Employee Detailes. . . 

def FetchEmpdata(request):
    context={}
    if request.method=="POST":
        empid=request.POST['EmpId']
        cur=connection.cursor() # temporary area to connect database from django.
        cur.execute('select * from employee3 where EmpId=%s',(empid,))
        data=cur.fetchall()
        #print(data)
        #return HttpResponse("I am a DBoperation app")
        context['empinfo']=data
        return render(request,'fetchdata.html',context)
    return render(request,'fetchdata.html')

# To insert The Employee Detailes by using ORM method. . . .

def orminsertdata(request):
    if request.method=='POST':
        ename=request.POST['empname']
        esal=request.POST['empsalary']
        eadd=request.POST['empaddress']
        
        emp=Employee(Employee_Name=ename,Employee_Salary=esal,Employee_Address=eadd)
        emp.save()
        
        return HttpResponse("Data Inserted Successfully")     
    return render(request,'insertemp.html')


def ormFetchData(request):
    data=Employee.objects.all()
    print(data)
    return HttpResponse('Data Retrieved')
    
# Inserting the Family Detailes into The Database. . .. 

def FamDetailes(request):
    if request.method=='POST':
        fathname=request.POST['fname']
        mothname=request.POST['mname']
        sonname=request.POST['sname']
        dau1name=request.POST['d1name']
        dau2name=request.POST['d2name']
        
        fdetailes=Family(FatherName=fathname,MotherName=mothname,SonName=sonname,Daughter_1_Name=dau1name,Daughter_2_Name=dau2name)
        fdetailes.save()
        return HttpResponse('Family created successfully')

    return render(request,'family.html')
    
# Fetching the Family detailes . . . .

def FetchFamdata(request):
    context={}
    if request.method=='POST':
        sname=request.POST['SonName']
        cur=connection.cursor()
        cur.execute('select * from ganeshdb1.DBoperations_Family where SonName=%s',(sname,))
        data=cur.fetchall()
        context['familyinfo']=data
        return render(request,'fetchfamily.html',context)
    return render(request,'fetchfamily.html')
    
# Inserting the Product Detailes into the Database. . . . 

def PDetailes(request):
    if request.method=="POST":
        company=request.POST['company']
        creams=request.POST['cream']
        scrubs=request.POST['scrub']
        lotions=request.POST['lotion']
        oils=request.POST['oil']
        gels=request.POST['gel']
        soaps=request.POST['soap']
        
        pdetailes=Product_Detailes(Product_Company=company,Cream_Base=creams,Scrub_Base=scrubs,
                                  Lotion_Base=lotions,Oil_Base=oils,Gel_Base=gels,Soap_Base=soaps)
        pdetailes.save()
        return HttpResponse("Detailes Added Successfully into DataBase")
    return render(request,'Products.html')

# Fetching the Product Detailes. . . . 

def fetchproduct(request):
    context={}
    if request.method =='POST':
        prod=request.POST['product']
        cur=connection.cursor()
        cur.execute('select * from ganeshdb1.dboperations_product_detailes where Product_Company=%s',(prod,))
        data=cur.fetchall()
        context['productinfo']=data
        return render(request,'fetchproduct.html',context)
    return render(request,'fetchproduct.html')

# Adding the Home Page. . . . 

def Homepage(request):
    return render(request,'home.html')


def formexp(request):
    if request.method=='POST':
        context={}
        context['form']=formexp()
        data=formexp(request.POST)
    return render(request,'formexp.html',context)


