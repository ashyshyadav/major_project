from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Exam, Question, Answer, Result
from classroom.models import Subject
from django.contrib.auth.decorators import login_required
from .forms import ExamCreationForm, AddQuestions
from django.contrib import messages 

# Create your views here.

# EXAM INDEX VIEW IT SHOW THE LIST OF EXAM FOR A PARTICULAR SUBJECT
@login_required
def index(request, subject):
    sub = Subject.objects.get(name=subject)
    user = request.user
    exams_taken = Result.objects.filter(user=user).values_list('exam_id', flat=True)
    new_exams = Exam.objects.filter(subject=sub.pk).exclude(id__in=exams_taken)
    completed_exam_list = []
    for exam_id in exams_taken:
        exam = Exam.objects.get(pk=exam_id)
        completed_exam_list.append(exam.name)
    context = {
        'subject': subject,
        'user':user,
        'exams_taken':exams_taken,
        'new_exam': new_exams,
        'completed_exam_list':completed_exam_list
    }
    return render(request,'exam/exam_index.html', context)
    
# EXAM INDEX VIEW ENDS HERE



@login_required
def exam(request, subject, exam_pk):
    if request.method == 'POST':
        score = 0
        exam = Exam.objects.get(pk=exam_pk)
        question_list = []
        get_correct_list =[]
        for question in exam.get_questions():
            question_list.append(question)
            get_correct = question.get_correct_answers()
            if get_correct == request.POST[question.text]:
                score = score + 1
            get_correct_list.append(get_correct)
        answer_input = []    
        for question in question_list:
            answer_input.append(request.POST[question.text])
        user = request.user
        score_in_percentage = (score/len(get_correct_list)) * 100
        result = Result(exam = exam, user = user, score = score_in_percentage)
        result.save()
        print(result)
        context = {
                'question_list':question_list,
                'answer_input': answer_input,
                'get_correct': get_correct,
                'get_correct_list': get_correct_list,
                'score':score,
                'scoreP': score_in_percentage,
                'username':user,
                'result': result
            }
        messages.success(request, "Your response has been recorded")    
        return HttpResponseRedirect('/user/profile/')       
    else:
        exam = Exam.objects.get(pk=exam_pk)
        # question_query = exam.get_questions() 
    
    
        context = {
            'subject': subject,
            'exam_pk': exam_pk,
            'exam':exam,
            # 'question_query': question_query,
            # 'question_list': question_list,
        }    
        return render(request,'exam/exam.html', context)




@login_required
def create_exam(request,subject):
    if request.method == 'POST':
        exam_creation_form = ExamCreationForm(request.POST)
        if exam_creation_form.is_valid():
            exam_creation_form.save()
            if exam_creation_form.save() :
                print("saved")
            else:
                print('not saved')    
            nubmer_of_questions = exam_creation_form.cleaned_data['number_of_questions']
            return redirect('add_questions', subject)
    else:
        exam_creation_form = ExamCreationForm()
        context = {
            'subject':subject,
            'exam_creation_form' :exam_creation_form
        }
        return render(request, 'exam/create_exam.html', context)


@login_required
def add_questions(request, subject):
    add_question_form = AddQuestions()
    context = {
        'test': 'hey',
        'subject': subject,
        'add_question_form': add_question_form,
    }
    return render(request, 'exam/add_questions.html', context)
