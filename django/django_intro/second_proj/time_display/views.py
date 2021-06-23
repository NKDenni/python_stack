from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%a %Y-%m-%d %H:%M %p", localtime())
    }
    return render(request, 'index.html', context)

# Create your views here.
