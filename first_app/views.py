from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def root(request):
    return render(request, 'root.html')


def hello(request):
    username = 'chanryeol'
    context = {
        'username': username,
    }
    return render(request, 'hello.html', context)


def lunch(request):
    menus = ['김밥', '돈까스', '라면', '쌀국수', '밥']
    pick = random.choice(menus)
    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)


def lotto(request):
    number = range(1, 46)
    pick = sorted(random.sample(number, 6))
    context = {
        'pick': pick,
    }

    return render(request, 'lotto.html', context)