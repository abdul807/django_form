from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse('hello world')

# app_name = 'detail'

def index(request):
    return render(request,'public/index.html'
        # "name" : name.capitalize()
    )


def signup(request):
    return render(request,'public/signup.html')