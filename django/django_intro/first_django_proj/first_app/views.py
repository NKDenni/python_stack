from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs.")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"Placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")

def destroy(request, num):
    return redirect('/')
# Create your views here.
