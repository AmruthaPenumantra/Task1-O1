from django.shortcuts import render
from django.http import HttpResponse
import json
import random

# Create your views here.

def index(request):
    return render(request, "index.html")


def hello_world(request):
    return HttpResponse("Hello world!")

def task(request):
    with open('myapp/Cartoon_char.json', 'r') as file:
        cartoon_characters = json.load(file)
    random_member = random.choice(cartoon_characters)
    context = {'cartoon': random_member}
    return render(request, 'task.html', context)
