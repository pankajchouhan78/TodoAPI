from django.urls import path
from .api import *

urlpatterns = [
    path('',ViewTodo),
    path('createtodo/',CreateTodo),
    path('UpdateTodo/<int:pk>',UpdateTodo,name="update"),
    path('delete/<int:pk>',DeleteTodo,name="delete"),
]