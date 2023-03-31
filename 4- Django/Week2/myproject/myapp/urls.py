from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.main),
    path('homepage/',views.homepage),
    path('year/',views.display_date),
    path('',views.menu,name='index'),
]