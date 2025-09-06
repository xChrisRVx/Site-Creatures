from django.shortcuts import render, redirect
import random

# Create your views here.
def brazileiro(request):
    numero = random.randint(1, 50)
    return render(request, 'br.html', {'numero': numero})

def ingles(request):
    numero = random.randint(1, 50)
    return render(request, 'en.html', {'numero': numero})

def menu(request):
    return render(request, 'menu.html')
