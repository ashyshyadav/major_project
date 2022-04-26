from django.db import models
from classroom.models import Subject
# Create your models here.
class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    points = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f'subject:{self.subject}, name:{self.name}'