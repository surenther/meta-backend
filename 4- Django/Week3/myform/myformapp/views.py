from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from myformapp.forms import Inputform

def form_view(request):
    form = Inputform()
    context = {'form':form}
    return render(request,"home.html",context)