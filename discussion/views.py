from django.shortcuts import render, HttpResponseRedirect
from .models import Message
from classroom.models import Subject
from . forms import MessageForm
from django.urls import reverse
# Create your views here.
def index(request, sub):
    subject = Subject.objects.get(name=sub)
    message_qs = Message.objects.filter(subject=subject).order_by('-id')
    context = {
        'message_qs': message_qs,
    }
    return render (request, 'discussion/index.html', context)

def create_message(request, sub):
    user = request.user
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            title = message_form.cleaned_data['title']
            message = message_form.cleaned_data['message']
            subject = Subject.objects.get(name=sub)
            discussion = Message(subject=subject, title=title, message=message, user=user)
            discussion.save()
            return HttpResponseRedirect(reverse('discussion-index', args=[subject]))
    else : 
        message_form = MessageForm()
        context = {
            'message_form': message_form
        }
        return render (request, 'discussion/create_message.html', context)       
    
