from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistrationPage, name = 'Registration-page'),
]