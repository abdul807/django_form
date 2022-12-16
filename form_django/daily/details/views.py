from django.shortcuts import render
from django.http import HttpResponse
from .models import Details
# Create your views here.


# def index(request):
#     return HttpResponse('hello world')



def index(request):
    all_names = Details.objects.all()
    print(all_names)
    return render(request,'public/index.html',
        # "name" : name.capitalize()
        {
            'names': all_names
        }
    )


def signup(request):

    return render(request,'public/signup.html')


def addData(request):
    name = request.POST.get('fname')
    email = request.POST.get('email')
    password = request.POST.get('password')

    detail = Details(name=name,email=email,password=password)
    detail.save()

    print(detail)
    return render(request, 'public/home.html')




def view_data(request):
    all_names = Details.objects.all()
    print(all_names)
    return render(request,'public/home.html',{ 
        'names':all_names
        })