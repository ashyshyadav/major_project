from os import name
from typing import Text
from django.forms.formsets import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Exam, Question, Answer, Result
from classroom.models import Subject
from django.contrib.auth.decorators import login_required
from .forms import ExamCreationForm, AddQuestions, AddAnswer, CustomQuestionForm
from django.contrib import messages 
from django.forms import modelformset_factory
# Create your views here.

# EXAM INDEX VIEW IT SHOWS THE LIST OF EXAM FOR A PARTICULAR SUBJECT
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
            pass
            # print(f"ELSE : EXAM.SUBJECT: {exam.subject}")    
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
        # print(f"-------------{request.POST}------------------")s
        score = 0
        exam = Exam.objects.get(pk=exam_pk)
        question_list = []
        get_correct_list =[]
        for question in exam.get_questions():
            question_list.append(question)
            get_correct = question.get_correct_answers()
            # print(f"-------question.get_correct_answers()--------{question.get_correct_answers()}")
            # print(f'_______QUESTION___{question}_____________')
            # print(f"-------POST------{request.POST[question.text]}------------------")
            # print(f"------get_correct-------{get_correct}-----get_correct_list-----{get_correct_list}")

            if get_correct == request.POST[question.text]:
                score = score + 1
                # print(f"-----------------{score}-------------")
            get_correct_list.append(get_correct)
        answer_input = []    
        for question in question_list:
            answer_input.append(request.POST[question.text])
        user = request.user
        score_in_percentage = (score/len(get_correct_list)) * 100
        result = Result(exam = exam, user = user, score = score_in_percentage)
        result.save()
        # print(result)
        messages.success(request, "Your response has been recorded")
        context = {
                'question_list':question_list,
                'answer_input': answer_input,
                'get_correct': get_correct,
                'get_correct_list': get_correct_list,
                'score':score,
                'scoreP': score_in_percentage,
                'username':user,
                'result': result,
            }
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
        user = request.user
        subject = user.teacher
        exam_creation_form = ExamCreationForm(request.POST)
        if exam_creation_form.is_valid():
            exam_creation_form.save()
            if exam_creation_form.save() :
                nubmer_of_questions = exam_creation_form.cleaned_data['number_of_questions']
                exam_name = exam_creation_form.cleaned_data['name']
                return redirect('add_questions', subject, exam_name, nubmer_of_questions)
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
    CustomFormset = formset_factory(CustomQuestionForm, extra=number_of_questions)
    exam =Exam.objects.get(name=exam_name)
    if request.method == 'POST':
        # customform = CustomQuestionForm(request.POST)
        formset = CustomFormset(request.POST)
        print(f'--------------{formset.is_valid()}-------')
        if formset.is_valid():
            for f in formset:   
                input_question = f.cleaned_data['question']
                input_option_1 = f.cleaned_data['option_1']
                input_option_2 = f.cleaned_data['option_2']
                input_option_3 = f.cleaned_data['option_3']
                input_option_4 = f.cleaned_data['option_4']
                input_correct  = f.cleaned_data['correct_option']
                print(f'---{input_question}---\n------{input_option_1}\n------{input_option_2}\n------{input_option_3}\n------{input_option_4}\n-----{input_correct}')
                question = Question(text=input_question, exam=exam)
                question.save()
                print(f"questio____{question}")
                print(type(input_correct))
                if input_correct == '1' :
                    co = input_option_1
                elif input_correct == '2' :                 
                    co = input_option_2 
                elif input_correct == '3' :
                    co = input_option_3
                elif input_correct == '4':
                    co = input_option_4 

                if co == input_option_1 :
                    answer_1 = Answer(text=input_option_1, correct=True, question=question)
                    answer_1.save()
                else :
                    answer_1 = Answer(text=input_option_1, correct=False, question=question)    
                    answer_1.save()

                if co == input_option_2 :
                    answer_2 = Answer(text=input_option_2, correct=True, question=question)
                    answer_2.save()
                else :
                    answer_2 = Answer(text= input_option_2, correct=False, question=question)
                    answer_2.save()

                if co == input_option_3 :
                    answer_3 = Answer(text=input_option_3, correct=True, question=question)
                    answer_3.save()
                else :  
                    answer_3 = Answer(text=input_option_3, correct=False, question=question)
                    answer_3.save()
                print(f'OUTSIDE-----------{input_correct}----------{input_option_4}---{co}')
                if co == input_option_4 :
                    print(f'{input_correct}-----EQUALS-----{input_option_4}')
                    answer_4 = Answer(text=input_option_4, correct=True, question=question)
                    answer_4.save()
                else :
                    answer_4 = Answer(text=input_option_4, correct=False, question=question)
                    answer_4.save()            
        context = {
        'cfs': CustomFormset
        }
        return redirect('/thankyou/')
    else:
        context = {
        'subject': subject,
        # 'add_question_form': add_question_form,
        # 'number_of_questions':number_of_questions,
        'exam_name':exam_name,
        # 'question_form_list': question_form_list
        'cfs': CustomFormset
    }
    
    return render(request, 'exam/add_questions.html', context)

def thankyou(request):
    return render(request, 'exam/create-exam-thankyou.html')