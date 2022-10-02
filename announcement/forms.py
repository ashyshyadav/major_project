from django import forms
from . models import Announcement
from django.contrib.auth.models import User
class CreateAnnouncement(forms.Form):
    title = forms.CharField( max_length=100, required=True)
    content = forms.CharField( max_length=1000, required=True, widget=forms.Textarea)
        

