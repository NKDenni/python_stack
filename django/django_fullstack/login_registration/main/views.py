from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.

def login_reg(request):
    return render(request, 'login_reg.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            messages.error(request, "Account already exists")
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
            birthday=request.POST['birthday'],
            password=hashed_pw
        )
        request.session['log_user'] = user1.id
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])

        if user:
            log_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['log_user'] = log_user.id
                return redirect('/success')
        messages.error(request, "Email or password is incorrect", extra_tags='log_user')
    return redirect("/")

def success(request):
    if request.method == "POST":
        context = {
            'log_user': User.objects.get(id=request.session['log_user'])
        }
        return render(request, 'success.html', context)
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
