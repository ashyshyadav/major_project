from venv import create
from . import views
from django.urls import path

urlpatterns = [
    path('create', views.create_syllabus, name='create-syllabus'),
    path('update-list', views.update_list, name='update-syllabus-list')  
]