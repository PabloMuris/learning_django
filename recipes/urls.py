from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('',views.home),
    path('recipes/<int:id>/',views.recipe),
]



