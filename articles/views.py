import imp
from unicodedata import name
from django.shortcuts import render
import random

# Create your views here.
def index(requset):
    return render(requset, 'index.html')

def dinner(request,name):
    menus = [{'name':'족발','price':30000},{'name':'치킨','price':19000},{'name':'피자','price':22500},{'name':'초밥','price':12000}]
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus':menus
    }
    return render(request, 'dinner.html',context)



def review(request):
    return render(request,'review.html')


def create_review(request):
    content = request.POST.get('content')
    print(request.POST)
    context = {
        'content':content,
    }
    return render(request, 'review_result.html',context)