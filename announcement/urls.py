from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='announcement-index'),
    path('create/', views.create_announcement, name='create-announcement')
]
