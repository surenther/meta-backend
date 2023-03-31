from django.urls import path
from viewsurl import views

urlpatterns = [
    path('dishes/<str:dish>', views.menuitems),
]