from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from generator.forms import *

import random

# Create your views here.
def home_page(request):
    return render(request, 'generator/home_page.html')

def password_generate(request):

    def generate(num, *args) -> str:
        # Функция для генерации паролей
        symbols_items = {
        'uppercase': 'QWERTYUIOPASDFGHJKLZXCVBNM',
        'lowercase': 'QWERTYUIOPASDFGHJKLZXCVBNM'.lower(),
        'numbers':'0123456789',
        'symbols':'!@#$%^&*()?'
        }
        settings_list = []

        if num > 120:
            return 'You input very big number'

        for item in args[0]:
            if item == True and args[0][0]:
                settings_list.append('uppercase')
            if item == True and args[0][1]:
                settings_list.append('lowercase')
            if item == True and args[0][2]:
                settings_list.append('numbers')
            if item == True and args[0][3]:
                settings_list.append('symbols') 
        
        if not bool(settings_list):
            return 'You dont select settings'

        temp = ''
        password = ''

        for key, values in symbols_items.items():
            for item in settings_list:
                if item == key:
                    temp += values
                    
        for _ in range(num):
            password += temp[random.randint(0, len(temp)-1)]
        
        return password

    
    context = {}

    if request.method == "POST":
        form = SettingsPassword(request.POST)
        num = 0
        if form.is_valid():
            uppercase = form.cleaned_data.get('uppercase')
            lowercase = form.cleaned_data.get('lowercase')
            numbers = form.cleaned_data.get('numbers')
            symbols = form.cleaned_data.get('symbols')
            num = form.cleaned_data.get('num')
            
            info = generate(num, [uppercase, lowercase, 
                                      numbers, symbols])
            
            context['info'] = [info, num]
    else:
        form=SettingsPassword()

    context['form'] = form

    return render(request, 'generator/password.html', 
                  context=context)


def numbers_generate(request):
    context = {}
    if request.method == "POST":
        form = RangeOfNumbers(request.POST)
        if form.is_valid():
            max_number = form.cleaned_data.get('max_num')
            min_number = form.cleaned_data.get('min_num')
            select = form.cleaned_data.get('float_or_int')
            decimal_places = form.cleaned_data.get('decimal_places')
            numbers = form.cleaned_data.get('numbers')
            meaning = []

            if select == True:
                for _ in range(numbers):
                    meaning.append(round(random.uniform(min_number, max_number),
                                          decimal_places))
            else:
                for _ in range(numbers):
                    meaning.append(random.randint(int(min_number), 
                                                  int(max_number)))                
                                
            context['info'] = [meaning, numbers, 
                               min_number, max_number, 
                               decimal_places]
    else:
        form = RangeOfNumbers()

    context['form'] = form

    return render(request, 'generator/numbers.html', 
                  context=context)


def about_page(request):
    return render(request, 'generator/about_page.html')