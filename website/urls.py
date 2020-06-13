from django.urls import path
from . import views

urlpatterns =[
    path('', views.home),
    path('contact', views.contact),
    path('rooms', views.rooms),
    path('index', views.index),
    path('cnfbooking', views.cnfbooking),
    path('home', views.home),
]