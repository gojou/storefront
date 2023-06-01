# Defines request handlers for Django implementation

from django.shortcuts import render
from django.http import HttpResponse
# from django.http import *

# Create your views here.

def say_hello(request) :
    # Original boring baby step
    # return HttpResponse('Hello Multiverse!')
    
    # Less boring. Look at the input and output parameters. "request" -> return object
    return render(request,'hello.html'
                # Testing testing - Pattern success!
                
                #  , {'name': 'Chaos'}
                  )
