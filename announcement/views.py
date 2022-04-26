from django.shortcuts import render, redirect
from . forms import CreateAnnouncement
from .models import Announcement
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    announcement_qs = Announcement.objects.all().order_by('-id')
    
    context = {
        'announcement_qs':announcement_qs,
        'subject':'announcement',
    }
    return render(request, 'announcement/index.html', context)

@login_required
def create_announcement(request):
    user = request.user
    teacher = user.teacher
    if request.method == 'POST':
        # print(True)
        create_announcement_form = CreateAnnouncement(request.POST)
        if create_announcement_form.is_valid() :
            # print(f"forms is valid")
            title = create_announcement_form.cleaned_data['title']
            content = create_announcement_form.cleaned_data['content']
            announcement = Announcement(title=title, content=content, teacher=teacher)
            announcement.save()
            # print(announcement)
            # print(f"{title} {content}")
        return redirect('/announcement/')
    else:
        create_announcement_form = CreateAnnouncement()
        context = {
            'create_announcement_form': create_announcement_form,
        }
        return render(request, 'announcement/create_announcement.html', context)
