from django.shortcuts import render, HttpResponseRedirect
from classroom.models import Subject
from . models import Assignment, Submission
from . forms import SubmissionForm, AssignmentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
@login_required
def index(request, subject):
    user = request.user
    sub = Subject.objects.get(name = subject)
    # exams_taken = Result.objects.filter(user=user).values_list('exam_id', flat=True)
    # new_exams = Exam.objects.filter(subject=sub.pk).exclude(id__in=exams_taken)
    submission = Submission.objects.filter(user=user).values_list('assignment_id', flat=True)
    new_assignment = Assignment.objects.filter(subject=sub).exclude(id__in=submission)
    assignment_qs = Assignment.objects.filter(subject = sub).order_by('-id')
    context = {
        'subject':sub,
        'assignment_qs': assignment_qs,
        'new_assignment':new_assignment
    }
    return render(request, 'assignment/index.html', context)

@login_required
def upload_assignment(request, pk):

    if request.method == 'POST':        
        submission_form = SubmissionForm(request.POST)
        if submission_form.is_valid():
            content = submission_form.cleaned_data['content']
            user = request.user
            assignment = Assignment.objects.get(pk = pk)
            submission = Submission(user=user, assignment=assignment, content=content)
            submission.save()
            subject = assignment.subject
            return HttpResponseRedirect(reverse('assignment-view', args=[subject]))
    else :
        submission_form = SubmissionForm()
        assignment = Assignment.objects.get(pk = pk)
        context = {
            'submission_form': submission_form,
            'assignment': assignment

        }
        return render (request, 'assignment/submission.html', context)
    

@login_required
def create_assignment(request):
    user = request.user
    teacher = user.teacher
    if request.method == 'POST':
        assignment_form = AssignmentForm(request.POST)
        if assignment_form.is_valid():
            title = assignment_form.cleaned_data['title']
            content = assignment_form.cleaned_data['content']
            subject = teacher.subject
            assignment = Assignment(subject=subject, title=title, content=content, teacher=teacher)
            assignment.save()
            return HttpResponseRedirect(reverse('assignment-view', args=[subject]))
    else : 
        assignment_form = AssignmentForm()
        context = {
            'assignment_form': assignment_form
        }
        return render (request, 'assignment/create-assignment.html', context)        


    