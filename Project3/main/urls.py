# urls.py
from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("diet/", views.diet, name="diet"),
path("quiz/", views.quiz, name="quiz"),
path("exercise/", views.exercise, name="exercise"),
path("analyze_diet/", views.analyzeDiet, name="analyze_diet"),
]