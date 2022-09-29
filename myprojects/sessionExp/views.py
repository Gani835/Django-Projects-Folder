from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

# Create your views here.

## Session: It stores the data in server side only.

def sessionfun(request,prodId):
    request.session.modified=True
    if 'visit' in request.session:
        request.session['visit']+=1
    else:
        request.session['visit']=1
        
        ## Another Example ##
        
    if 'product' in request.session:
        request.session['products'].append(prodId)
    else:
        request.session['products']=[prodId]
        
    print(request.session['products'])
    
    #return HttpResponse(f"I am activated {request.session['visit']}")

## Cookies:It stores the data in client side only. . . .

    resp=HttpResponse(f"I am activated {request.session['visit']}")
    resp.set_cookie('cookie','I am a COOKIE')
    return resp

## It was not completed. . ..