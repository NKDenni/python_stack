from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note
from .forms import NoteForm

# Create your views here.
def my_post(request):
    context = {
        'notes': Note.objects.all().order_by("-id"),
        'new_note': NoteForm(),
    }
    return render(request, 'myposts.html', context)

def new_note(request):
    if request.method == "POST":

        bound_form = NoteForm(request.POST)

        if bound_form.is_valid():
            this_note = Note.objects.create(text=request.POST['text'])

    context = {
        'notes': Note.objects.all().order_by("-id")
    }
    return render(request, 'note_index.html', context)

def delete(request, id):
    this_post = Note.objects.get(id=id)
    this_post.delete()
    return redirect('/')
