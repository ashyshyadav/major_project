from django.urls import path
from . import views
urlpatterns = [
    path('<str:sub>', views.index, name='discussion-index'),
    path('create/<str:sub>/', views.create_message, name='discussion-create')
]
