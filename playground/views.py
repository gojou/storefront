# Defines request/response handlers for this Django implementation

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def say_hello(request) :
    # Original boring baby step
    # return HttpResponse('Hello Multiverse!')
    
    # Less boring. Look at the input and output parameters. "request" -> return object
    return render(request,'hello.html',{'name':'Gimp'})
