from multiprocessing import context
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from django.db import connection
from.models import Amazonproducts
from.forms import productsform
# Create your views here.

def amazonprod(request):
    if request.method=='POST':
        prdid=request.POST['prodid']
        prdname=request.POST['prodname']
        prdprice=request.POST['prodprice']
        prodinfo=Amazonproducts(prodId=prdid,prodname=prdname,prodprice=prdprice)
        prodinfo.save()
        return HttpResponse('Detailes are saved Successfully. . . .')
    return render(request,'amazon.html')
    #return HttpResponse('Welcome to Amazon. . . .')
    
def fetchprod(request):
    context={}
    data=Amazonproducts.objects.all()
    context['info']=data
    return render(request,'fetchprod.html',context)

def prodform(request):
    context={}
    form=productsform()
    context['form']=form
    if request.method=='POST':
        data=productsform(request.POST)
        if data.is_valid():
            prdid=data.cleaned_data['prodId']
            prdname=data.cleaned_data['prodname']
            prdprice=data.cleaned_data['prodprice']
            prodinfo=Amazonproducts(prodId=prdid,prodname=prdname,prodprice=prdprice)
            
            data.save()
            return HttpResponse('Data stored successfully. . . .')
        else:
            return HttpResponse('Data was not stored. . . .')
    return render(request,'prodform.html',context)