from django.shortcuts import render, redirect
from . forms import  CreateSyllabus
from django.http import HttpResponse
from django.views.generic import ListView
from classroom.models import Curriculum
# Create your views here.

def update_list(request):
    teacher = request.user.teacher
    subject = teacher.subject
    syllabus_qs = Curriculum.objects.filter(subject = subject)
    context = {
        'teacher': teacher,
        'subject':subject,
        'syllabus_qs': syllabus_qs,
    }
    return render (request, 'syllabus/update-list.html', context)


def create_syllabus(request):
    if request.method == 'POST':
        create_syllabus = CreateSyllabus(request.POST)
        if create_syllabus.is_valid():
            print(f"  {create_syllabus.cleaned_data['chapter']}---------{create_syllabus.cleaned_data['subject']}-----------{create_syllabus.cleaned_data['is_complete']}-----------{create_syllabus.cleaned_data['completion_date']}") 
        return redirect ('syllabus/successfull.html')
    else :
        create_syllabus = CreateSyllabus()
        context = {
            'create_syallbus': create_syllabus
        }
        return render(request, 'syllabus/create_syllabus.html', context=context)

