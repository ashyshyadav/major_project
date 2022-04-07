from django.shortcuts import render, redirect
from . forms import  CreateSyllabus
# Create your views here.
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