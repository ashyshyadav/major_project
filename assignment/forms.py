from django import forms


class SubmissionForm(forms.Form):
    content = forms.CharField(max_length=5000, required=True, widget=forms.Textarea)

class AssignmentForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    content = forms.CharField(max_length=5000, required=True, widget=forms.Textarea)