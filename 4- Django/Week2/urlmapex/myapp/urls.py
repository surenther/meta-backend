from django.urls import path
from myapp import views

urlpatterns = [
    path('drinks/<str:drink>', views.drinks,name='drink'),
]
