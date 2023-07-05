from django.contrib import admin
from django.urls import path

from generator.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('psswd_gen', password_generate, name = 'generate_password'),
    path('numbers_gen', numbers_generate, name = 'numbers_generate'),
    path('about', about_page, name='about_page'),
]
