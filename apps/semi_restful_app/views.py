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
        Dog.objects.create(name=name, age=age, color=color, size=size, fixed=fixed, vaccine=vaccine, adopted=adopted)
    return redirect('/')

def select(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    avail_dogs = Dog.objects.exclude(adopted=True)
    print current_dog
    context = {
        "avail_dogs" : avail_dogs,
        'current_dog' : current_dog,

    }
    return render(request, 'semi_restful_app/index.html', context)

def select_adopted(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    adopted_dogs = Dog.objects.filter(adopted=True)
    print current_dog
    context = {
        "adopted_dogs" : adopted_dogs,
        'current_dog' : current_dog,

    }
    return render(request, 'semi_restful_app/adopted.html', context)

def adopted(request, dog_id):
    adopted_dog = Dog.objects.get(id=dog_id)
    adopted_dog.adopted = True
    adopted_dog.save()

    return redirect('/')

def adopted_dogs(request):
    adopted_dogs = Dog.objects.filter(adopted=True)
    context = {

        'adopted_dogs' : adopted_dogs

    }

    return render(request, 'semi_restful_app/adopted.html', context)

def available(request, dog_id):
    available_dog = Dog.objects.get(id=dog_id)
    available_dog.adopted = False
    available_dog.save()

    return redirect('/adopted_dogs')