from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def drinks(request,drink):
    item = {
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment',
    } 
    description = item[drink]
    return HttpResponse (f"<h2> {drink} </h2> <br>" + description)