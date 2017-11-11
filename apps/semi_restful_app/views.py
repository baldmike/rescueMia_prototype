from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from django.core.urlresolvers import reverse
 
from models import *

def index(request):
    context = {
        "avail_dogs" : Dog.objects.exclude(adopted=True),
    }
    return render(request, 'semi_restful_app/index.html', context)

def new_dog(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        color = request.POST['color']
        size = request.POST['size']
        fixed = request.POST['fixed']
        vaccine = request.POST['vaccine']
        adopted = False
        Dog.objects.create(name=name, age=age, color=color, size=size, fixed=fixed, vaccine=vaccine)
    return redirect('/')

def select(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    print current_dog
    context = {
        "avail_dogs" : Dog.objects.exclude(adopted=True),
        'current_dog' : current_dog,

    }
    return render(request, 'semi_restful_app/index.html', context)