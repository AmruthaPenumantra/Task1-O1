from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index),
    path('task',views.task,name="task"),
]

# localhost:8000/hello