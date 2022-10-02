from datetime import datetime
from django.db import models
from classroom.models import Subject
from users.models import Teacher
from django.contrib.auth.models import User
# Create your models here.
class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f'subject:{self.subject}, name:{self.title}'

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'subject:{self.user}, name:{self.assignment}'