"""The url of the scheme for learning_logs"""
from django.urls import path
from . import views

app_name = 'shedule'
urlpatterns = [
    path('', views.index, name='index'),
]
