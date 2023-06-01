# Maps URLs to "views" (request handlers)

from django.urls import path
from . import views

# IMPORTANT: 
#   "urlpatterns" is a variable referenced by django so 
#   creativity is a big no-no here. 
#
#URLConf -> URL Configuration ***duh***

urlpatterns = [
    path('hello/',views.say_hello)
]