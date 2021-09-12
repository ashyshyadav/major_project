from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="exam-index"),
    path('<int:exam_pk>/', views.exam, name="exam-view")
]
