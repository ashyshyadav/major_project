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
        labels = {
            "text": "Question"
        }

class AddAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        exclude =('question',)
        

class CustomQuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)
    option_1 = forms.CharField(max_length=200)
    option_2 = forms.CharField(max_length=200)
    option_3 = forms.CharField(max_length=200)
    option_4 = forms.CharField(max_length=200)
    CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    correct_option = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)