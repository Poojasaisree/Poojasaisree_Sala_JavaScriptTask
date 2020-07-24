from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def RegistrationPage(request):
    return render(request,'JavaScript/RegistrationPage.html')

