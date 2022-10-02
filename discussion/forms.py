from django import forms



class MessageForm(forms.Form):
    title = forms.CharField(max_length=200)
    message = forms.CharField(max_length=5000, required=True, widget=forms.Textarea)

