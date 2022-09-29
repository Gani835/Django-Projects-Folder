from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
    return render(request,'welcome.html')

def page2(request):
    return render(request,'step1.html')

def page3(request):
    return render(request,'step2.html')

def page4(request):
    return render(request,'homepage.html')