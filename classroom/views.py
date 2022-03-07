from os import name
from typing import ContextManager
from django.http.response import Http404
from django.shortcuts import render
from . models import Subject
def index(request, subject):
    # try:
        template_path = "classroom/" + subject + ".html"
        active_page = subject
        c_list = []
        sub = Subject.objects.get(name=subject)
        print(f'--------{sub.get_curriculums()}')
        for c in sub.get_curriculums():
            c_list.append(c)
        context ={
            'subject':subject,
            'active_page':active_page,
            'c_list': c_list
        }
        
        return render (request, template_path, context)
    # except:    
        # raise Http404("Page not found")    
    

def welcome(request):
    return render(request, 'classroom/welcome.html')