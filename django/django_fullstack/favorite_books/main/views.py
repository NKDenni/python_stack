from django.contrib.messages.api import error
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def login_reg(request):
    return render(request, 'login_reg.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            messages.error(request, "Email already exists", extra_tags='email')
            return redirect('/')

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')

        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user1 = User.objects.create(
            first=request.POST['first'],
            last=request.POST['last'],
            email=request.POST['email'],
            password=hashed_pw
        )
        request.session['log_user'] = user1.id
        return redirect('/books')
    return redirect('/')


def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            log_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['log_user'] = log_user.id
                return redirect('/books')
        messages.error(request, "Email or password is incorrect", extra_tags='log_user')
    return redirect("/")


def logout(request):
    request.session.clear()
    return redirect('/')


def books(request):
    if 'log_user' not in request.session:
        request.session.clear()
        return redirect('/')

    context = {
        'log_user': User.objects.get(id=request.session['log_user']),
        'books': Book.objects.all(),
    }

    return render(request, 'books.html', context)


def new_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        user = User.objects.get(id=request.session['log_user'])

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/books')

        book1 = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploaded_by=user,
        )

        user.liked_books.add(book1)
        
    return redirect('/books')


def details(request, id):
    if 'log_user' not in request.session:
        request.session.clear()
        return redirect('/')

    context = {
        'log_user': User.objects.get(id=request.session['log_user']),
        'this_book': Book.objects.get(id=id),
    }
    return render(request, 'details.html', context)


def add(request,id):
    if 'log_user' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['log_user'])
    book = Book.objects.get(id=id)
    user.liked_books.add(book)

    return redirect('/books')

def remove(request, id):
    if 'log_user' not in request.session:
        request.session.clear()
        return redirect('/')

    user = User.objects.get(id=request.session['log_user'])
    book = Book.objects.get(id=id)
    user.liked_books.remove(book)

    return redirect(f'/books')


def update(request, id):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        user = User.objects.get(id=request.session['log_user'])

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect(f'/books/{id}')
        this_book = Book.objects.get(id=id)
        this_book.title=request.POST['title']
        this_book.desc=request.POST['desc']
        this_book.save()

    return redirect(f'/books/{id}')


def delete(request, id):
    if 'log_user' not in request.session:
        request.session.clear()
        return redirect('/')
    if request.method != "POST":
        return redirect('/books')

    log_user = User.objects.get(id=request.session['log_user'])
    this_book = Book.objects.get(id=id)

    print(log_user)
    print(this_book.uploaded_by)

    if log_user == this_book.uploaded_by:
        this_book.delete()

    return redirect('/books')
