from django.contrib.admin import widgets
from django import forms 
from classroom.models import Curriculum


class CreateSyllabus(forms.ModelForm):
    class Meta :
        model = Curriculum
        fields = '__all__'
        widgets = {
            'completion_date': widgets.AdminDateWidget
        }
    