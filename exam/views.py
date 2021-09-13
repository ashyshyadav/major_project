from django.shortcuts import render
from .models import Exam, Question, Answer, Result
from classroom.models import Subject
from django.contrib.auth.decorators import login_required
from .forms import ExamCreationForm
# Create your views here.

def index(request, subject):
    sub = Subject.objects.get(name=subject)
    sub_pk = sub.pk
    exams = Exam.objects.filter(subject=sub_pk)
    context = {
        'exams' : exams,
        'subject': subject
    }
    return render(request,'exam/exam_index.html', context)
    
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
        testAnswer = Answer.objects.get(text=answer_input[0])   
        testAnswer = testAnswer.correct
        username = request.user
        score_in_percentage = (score/len(get_correct_list)) * 100
        context = {
                'question_list':question_list,
                'answer_input': answer_input,
                'test_answer': testAnswer ,
                'get_correct': get_correct,
                'get_correct_list': get_correct_list,
                'score':score,
                'scoreP': score_in_percentage,
                'username':username,
            }   
        return render (request, 'exam/submit.html', context)
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
    exam_creation_form = ExamCreationForm()
    context = {
        'subject':subject,
        'exam_creation_form' :exam_creation_form
    }
    return render(request, 'exam/create_exam.html', context)