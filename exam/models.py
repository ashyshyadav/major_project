from django.db import models
from classroom.models import Subject
from django.contrib.auth.models import User
# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=120)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    number_of_questions = models.IntegerField()
    required_score_pass =models.IntegerField(default=40,)
    time = models.IntegerField(help_text="duration of test in minutes")

    
    def __str__(self):
        return f"{self.subject}: {self.name}"

    def get_questions(self):
        return self.question_set.all()

   

class Question(models.Model):
    text = models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exam.name}: {self.text}"

    def get_answers(self):
        return self.answer_set.all()

    def get_correct_answers(self):
        for answers in self.get_answers():
            if answers.correct:
                return answers.text
       

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question =models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f" question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

