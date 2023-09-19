# openaiapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('get_openai_response/', views.get_openai_response, name='get_openai_response'),
]

