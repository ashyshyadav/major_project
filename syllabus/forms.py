from django import forms 
from classroom.models import Curriculum


class CreateSyllabus(forms.ModelForm):
    class Meta :
        model = Curriculum
        fields = '__all__'
        widgets = {
            'completion_date' : forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }
    
class UpadateSyllabus(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['is_complete', 'completion_date']    
        widgets = {
            'completion_date' : forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }