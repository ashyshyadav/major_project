from os import name
from typing import Text
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Exam, Question, Answer, Result
from classroom.models import Subject
from django.contrib.auth.decorators import login_required
from .forms import ExamCreationForm, AddQuestions, AddAnswer, CustomQuestionForm
from django.contrib import messages 
from django.forms import modelformset_factory
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
        if str(exam.subject) == subject:
            completed_exam_list.append(exam.name)
        else:
            print(f"ELSE : EXAM.SUBJECT: {exam.subject}")    
    context = {
        'subject': subject,
        'user':user,
        'exams_taken':exams_taken,
        'new_exam': new_exams,
        'completed_exam_list':completed_exam_list,
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
                nubmer_of_questions = exam_creation_form.cleaned_data['number_of_questions']
                exam_name = exam_creation_form.cleaned_data['name']
                return redirect('add_questions', subject, exam_name, nubmer_of_questions)
                print("saved")
            else:
                print('not saved')                
    else:
        exam_creation_form = ExamCreationForm()
        context = {
            'subject':subject,
            'exam_creation_form' :exam_creation_form
        }
        return render(request, 'exam/create_exam.html', context)
        
@login_required
def add_questions(request, subject, exam_name, number_of_questions): 
    QuestionFormSet = modelformset_factory(Question, fields=('text',), extra = number_of_questions)
    customform = CustomQuestionForm()
    form = QuestionFormSet()
    if request.method == 'POST':
        customform = CustomQuestionForm(request.POST)
        if customform.is_valid():
            print('TRUE--------------')
            q1 = customform.cleaned_data['question']
            a1 = customform.cleaned_data['option_1']
            a2 = customform.cleaned_data['option_2']
            a3 = customform.cleaned_data['option_3']
            a4 = customform.cleaned_data['option_4']
            c = customform.cleaned_data['correct_option']
            if c == 1 :
                co = a1
            elif c == 2 :
                co = a2 
            elif c == 3 :
                co = a3
            else:
                co = a4    
            exam = Exam.objects.get(name=exam_name)    
            question = Question(text=q1, exam=exam)
            question.save()

            if co == a1 :
                answer_1 = Answer(text=a1, correct=True, question=question)
                answer_1.save()
            else :
                answer_1 = Answer(text=a1, correct=False, question=question)    
                answer_1.save()
            if co == a2 :
                answer_2 = Answer(text=a2, correct=True, question=question)
                answer_2.save()
            else :
                answer_2 = Answer(text=a2, correct=False, question=question)
                answer_2.save()
            if co == a3 :
                answer_3 = Answer(text=a3, correct=True, question=question)
                answer_3.save()
            else :
                answer_3 = Answer(text=a3, correct=False, question=question)
                answer_3.save()
            if co == a4 :
                answer_4 = Answer(text=a4, correct=True, question=question)
                answer_4.save()
            else :
                answer_4 = Answer(text=a4, correct=False, question=question)
                answer_4.save()
            print(question)    
            print(f'{q1}-------------{a1}--{a2}--{a3}--{a4}--{c}--{a4}')

        else:
            print('FALSE--------------')    
        context = {
        'form' : form,  
        'cf': customform
        }
        return redirect('/thankyou/')
    else:
        add_questions = AddQuestions()
        answer_1 = AddAnswer(prefix='answer_1')
        answer_2 = AddAnswer(prefix='answer_2')
        answer_3 = AddAnswer(prefix='answer_3')
        answer_4 = AddAnswer(prefix='answer_4')
        
        context = {
        'form' : form,    
        'add': add_questions,
        'a1': answer_1,
        'a2': answer_2,
        'a3': answer_3,
        'a4': answer_4,
        'subject': subject,
        # 'add_question_form': add_question_form,
        # 'number_of_questions':number_of_questions,
        'exam_name':exam_name,
        # 'question_form_list': question_form_list
        'cf': customform
    }
    
    return render(request, 'exam/add_questions.html', context)
