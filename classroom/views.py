from typing import ContextManager
from django.http.response import Http404
from django.shortcuts import render

def index(request, subject):
    # try:
        template_path = "classroom/" + subject + ".html"
        active_page = subject
        context ={
            'subject':subject,
            'active_page':active_page
        }
        
        return render (request, template_path, context)
    # except:    
        # raise Http404("Page not found")    
    

def welcome(request):
    return render(request, 'classroom/welcome.html')