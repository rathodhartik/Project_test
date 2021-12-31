from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


# Template use

def base1(request):
    return render(request,"base1.html")



def home(request):
     return render(request,'home.html')


def homepage(request):
    return render(request,'homepage.html')
