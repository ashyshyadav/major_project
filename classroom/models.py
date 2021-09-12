from contextlib import redirect_stdout
from django.db import models

# Create your models here.
class Subject(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Curriculum(models.Model):
    chapter = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.subject} : {self.chapter} "

