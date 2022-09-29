from django.shortcuts import render,HttpResponse

# Create your views here.

def calculator(request):
    return render(request,"calc.html")