from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def change_content(request):
    return render(request,'changecontent.html')

def dialogue_box(request):
    return render(request,'dialoguebox.html')

def change_image(request):
    return render(request,'changeimg.html')

# Javascript Validation. . . . 

def jsvalidate(request):
    if request.method=='POST':
        num=request.POST['val']
        if int(num)>0:
            return HttpResponse('Positive Number')
        else:
            return HttpResponse('Negative Number')
        
    return render (request,'jsvalidate.html')