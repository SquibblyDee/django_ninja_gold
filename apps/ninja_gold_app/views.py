from django.shortcuts import render, redirect
import random
import datetime
import time

# Initialize our session keys if needed
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['building'] = "initial"
        request.session['activities'] = []
        request.session['goldEarned'] = 0
        request.session['datetime'] = ""
    return render(request,'ninja_gold_app/index.html')

def process_money(request, methods=['POST']):
    # Determine how much gold we win or lose
    request.session['building'] = request.POST['building']
    if request.session['building'] == 'farm':
        request.session['goldEarned'] = random.randint(10,20)
    elif request.session['building'] == 'cave':
        request.session['goldEarned'] = random.randint(5,10)
    elif request.session['building'] == 'house':
        request.session['goldEarned'] = random.randint(2,5)
    else:
        request.session['goldEarned'] = random.randint(-50,50)
    request.session['gold'] += request.session['goldEarned']
    # Append all of our needed things from the session key into a lovely dictionary that we first need to turn into a temp var
    temp_list = request.session['activities']
    request.session['datetime'] = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
    temp_list.append({"gold": request.session['gold'], "building": request.session['building'], "goldEarned": request.session['goldEarned'], "datetime": request.session['datetime']})
    request.session['activities'] = temp_list
    return redirect('/')


def destroy(request):
    request.session.clear()
    return redirect('/')