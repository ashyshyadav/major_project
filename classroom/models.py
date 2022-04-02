from contextlib import redirect_stdout
from os import name
from django.db import models
import datetime
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    def get_curriculums(self):
        return self.curriculums.all()    

class Curriculum(models.Model):
    chapter = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='curriculums')
    is_complete = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f"{self.subject} : {self.chapter} "

