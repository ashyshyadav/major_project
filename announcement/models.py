from datetime import datetime
from email.policy import default
from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone
from users.models import Teacher
# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title