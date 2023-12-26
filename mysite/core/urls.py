from django.urls import path
from . import views

urlpatterns = [
    path('hacker/', views.hacker, name='hacker'),
]