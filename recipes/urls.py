from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from recipes.views import *


urlpatterns = [
    path('',Myview),
    path('sobre/',sobre),
    path('contato/',contato),
]