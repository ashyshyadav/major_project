from exam.models import Result, Exam
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm , ProfileUpdateForm
from django.contrib import messages 
from classroom.models import Curriculum, Subject
from assignment.models import Submission
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

# Create your views here.

# REGISTER VIEW, IT IS FOR USER REGISTRATION
def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST) 
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('welcome')
        context = {
            'register_form':register_form
        }
        return render(request, 'users/register.html', context)
    else :
        register_form = UserRegisterForm()
        context = {
            'register_form':register_form
        }
        return render(request, 'users/register.html', context)    

# REGISTER VIEW ENDS HERE


# USER PROFILE VIEW 
@login_required
def profile(request):
    user = request.user
    try : 
        check_teacher = user.teacher
    except ObjectDoesNotExist:
        check_teacher = False    
    if (check_teacher):
        subject = user.teacher.subject
        exams = Exam.objects.filter(subject=subject)
        result_query_list = []
        for e in exams :
            result_query_list.append(Result.objects.filter(exam=e))
            
        completed = Curriculum.objects.filter(subject=subject, is_complete=True).count()
        pending = Curriculum.objects.filter(subject=subject, is_complete=False).count()
        completed_qs = Curriculum.objects.filter(subject=subject, is_complete=True)
        line_data =[]
        jan_chp = 0
        feb_chp = 0
        mar_chp = 0
        apr_chp = 0
        for q in completed_qs:
  
            if q.completion_date.month == 1:
                jan_chp = jan_chp + 1
            elif q.completion_date.month == 2:
                feb_chp = feb_chp + 1
            elif q.completion_date.month == 3:
                mar_chp = mar_chp + 1
            elif q.completion_date.month == 4:
                apr_chp = apr_chp + 1     
        line_data.append(jan_chp)  
        line_data.append(feb_chp) 
        line_data.append(mar_chp) 
        line_data.append(apr_chp)       
        context = {
            'feb_chp': feb_chp,
            'jan_chp':jan_chp,
            'completed':completed,
            'pending': pending,
            'line_data':line_data,
            'user': user,
            'subject': subject, 
            'result_query_list': result_query_list,     
        }
        return render(request, 'users/teacher_dashboard.html', context)
    
    result = Result.objects.filter(user = user)
    submission = Submission.objects.filter(user=user)
    python = Subject.objects.get(name='python')
    multimediasystem = Subject.objects.get(name='multimediasystem')
    dbms = Subject.objects.get(name='dbms') 
    microprocessor = Subject.objects.get(name='microprocessor')  
    python_pending = Curriculum.objects.filter(subject=python, is_complete=False).count()
    python_completed = Curriculum.objects.filter(subject=python, is_complete=True).count()
    multimediasystem_pending = Curriculum.objects.filter(subject=multimediasystem, is_complete=False).count()
    multimediasystem_completed = Curriculum.objects.filter(subject=multimediasystem, is_complete=False).count()
    dbms_pending = Curriculum.objects.filter(subject=dbms, is_complete=False).count()
    dbms_completed = Curriculum.objects.filter(subject=dbms, is_complete=True).count()
    microprocessor_pending = Curriculum.objects.filter(subject=microprocessor, is_complete=False).count()
    microprocessor_completed = Curriculum.objects.filter(subject=microprocessor, is_complete=True).count()
    
    context={
        'user':user,
        'result':result,
        'python_pending': python_pending,
        'python_completed': python_completed,
        'multimediasystem_pending': multimediasystem_pending,
        'multimediasystem_completed': multimediasystem_completed,
        'dbms_pending': dbms_pending,
        'dbms_completed': dbms_completed,
        'microprocessor_pending': microprocessor_pending,
        'microprocessor_completed': microprocessor_completed,
        'submission': submission,
    }   
    return render(request, 'users/profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile is successfully Updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form   
    }

    return render(request , 'users/updateprofile.html', context)


