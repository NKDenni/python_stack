from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request,'new.html')

def submit(request):
    print(request.POST['release_date'])
    errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/new')
    else:
        this_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
    return redirect(f'/shows/{this_show.id}')

def show_details(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }
    return render(request, 'show_details.html', context)


def edit(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }

    return render(request, 'edit.html', context)

def update(request, id):
    print(request.POST['release_date'])
    errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{id}/edit')
    else:
        this_show = Show.objects.get(id=id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.desc = request.POST['desc']
        this_show.save()
        messages.success(request, "Show successfully updated")
    return redirect(f'/shows/{id}')

def destroy(request, id):
    this_show = Show.objects.get(id=id)
    this_show.delete()
    
    return redirect('/shows')
# Create your views here.
