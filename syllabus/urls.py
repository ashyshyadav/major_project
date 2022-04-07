from venv import create
from . import views
from django.urls import path

urlpatterns = [
    path('create-syllabus', views.create_syllabus, name='create-syllabus')
]