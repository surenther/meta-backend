from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def main (request):
    return HttpResponse('Hello World')

def homepage (request):
    return HttpResponse('This is homepage')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = '<h1 style ="color: #f4ce14;"> This is page is developed in Django </h1>'
    return HttpResponse(text)