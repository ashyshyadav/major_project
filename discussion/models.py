from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from classroom.models import Subject
# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
