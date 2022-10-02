from django.urls import path
from . import views

urlpatterns = [
    path('subject/<str:subject>/', views.index, name='assignment-view'),
    path('<int:pk>/upload/', views.upload_assignment, name='assignment-upload'),
    path('create/', views.create_assignment, name='assignment-create')
]