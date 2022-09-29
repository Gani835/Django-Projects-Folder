from django.shortcuts import render
from django.http import HttpResponse
from revision.models import products
# Create your views here.

def bootstrapexp(request):
    context={}
    info=products.objects.all()
    context['products']=info
    #return HttpResponse('Welcome to Bootstrap App')
    return render (request,'index.html')