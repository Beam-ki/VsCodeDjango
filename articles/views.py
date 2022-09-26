import imp
from django.shortcuts import render
import random

# Create your views here.
def index(requset):
    return render(requset, 'index.html')

def dinner(request):
    menus = ['족발','치킨','피자','초밥']

    pick = random.choice(menus)
    context = {
        'pick' : pick
    }
    return render(request, 'dinner.html',context)