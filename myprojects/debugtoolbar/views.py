from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def debugexp(request):
    return render(request,'debug.html')