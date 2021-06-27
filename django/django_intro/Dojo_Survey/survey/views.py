from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def submit(request):
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['description'] = request.POST['description']

    return redirect('/result')

def result(request):
    context = {
        'first_name': request.session['first_name'],
        'last_name': request.session['last_name'],
        'language': request.session['location'],
        'special': request.session['language'],
        'description': request.session['description'],
    }

    return render(request,'result.html', context)
# Create your views here.
