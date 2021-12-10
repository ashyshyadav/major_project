from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="exam-index"),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('add_questions/<str:exam_name>/<int:number_of_questions>', views.add_questions, name='add_questions'),
    path('<int:exam_pk>/', views.exam, name="exam-view"),
]
