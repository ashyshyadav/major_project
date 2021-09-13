from django import forms
from django.forms import fields 
from . models import Exam 

class ExamCreationForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('name', 'subject', 'number_of_questions', 'required_score_pass', 'time')