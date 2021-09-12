from django.contrib import admin
from .models import Exam,Question,Answer,Result
# Register your models here.
admin.site.register(Exam)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines =[AnswerInline]

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)    