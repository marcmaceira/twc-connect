from django.contrib import admin
from django.urls import path
from events import views
from django.conf.urls import url, include
from django.http import HttpResponse

urlpatterns = [
    path('art/', views.art),
    path('business/', views.business),
    path('food-and-drink/', views.food),
    path('government/', views.government),
    path('happy-hour/', views.happyHour),
    path('science-and-tech/', views.stem),
]