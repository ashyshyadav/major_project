from django import forms
from django.forms import fields 
from . models import Exam, Question, Answer

class ExamCreationForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('name', 'subject', 'number_of_questions', 'required_score_pass', 'time')


class AddQuestions(forms.ModelForm):
    class Meta:
        model =  Question
        fields = '__all__'
        exclude = ['exam']

class AddAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        exclude =('question',)
        