from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

def index(request):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def new_game(request):
    request.session.clear()
    return redirect("/")

def process_money(request):
    location = request.POST['location']
    
    amount = {
        'farm': (10,20),
        'mine': (10,30),
        'house': (0,5),
        'casino': (-50,50)
    }

    range_of_amount = amount[location]
    inhand = request.session['current_gold']
    gold = randint(range_of_amount[0], range_of_amount[1])
    transaction_time = datetime.now().strftime("%m/%d/%Y %I:%M%p")

    if location == 'casino' and inhand < 50:
        message = f"Uh-oh you don't have enough money to play. Bouncer kicked you out"
        request.session['current_gold'] = inhand
    elif gold < 0 and inhand >= abs(gold):
        message = f"Uh-Oh you lost {abs(gold)} gold from the {location}! ({transaction_time})"
        request.session['current_gold'] += gold
    else:
        message = f"Earned {abs(gold)} gold from the {location}! ({transaction_time})"
        request.session['current_gold'] += gold

    request.session['activities'].append(message)
    
    return redirect('/')
# Create your views here.
