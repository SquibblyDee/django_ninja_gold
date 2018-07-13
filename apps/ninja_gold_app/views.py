from django.shortcuts import render, redirect
import random
import datetime
import time

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['building'] = "initial"
        request.session['activities'] = []
        request.session['goldEarned'] = 0
        request.session['datetime'] = ""
    return render(request,'ninja_gold_app/index.html')

def process_money(request, methods=['POST']):
    print("WE IN PROCESS MONEY")
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
    temp_list = request.session['activities']
    request.session['datetime'] = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
    temp_list.append({"gold": request.session['gold'], "building": request.session['building'], "goldEarned": request.session['goldEarned'], "datetime": request.session['datetime']})
    request.session['activities'] = temp_list
    print(request.session['activities'])
    return redirect('/')
    # if request.session['goldEarned'] > 0:
        # temp_list = request.session['activities']
        # request.session['datetime'] = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
        # temp_list.append({"gold": request.session['gold'], "building": request.session['building'], "goldEarned": request.session['goldEarned'], "datetime": request.session['datetime']})
        ## temp_list.append("Earned "+str(request.session['goldEarned'])+" gold from the "+request.session['building']+"!  ("+str(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))+")")
        # request.session['activity'] = temp_list
        ##request.session['activity']="Earned "+str(request.session['goldEarned'])+" gold from the "+request.session['building']+"!  ("+str(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))+")\n"
    # else:
        # temp_list = request.session['activity']
        # request.session['datetime'] = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
        # temp_list.append("Entered a "+request.session['building']+" and lost "+str(request.session['goldEarned'])+" gold... Ouch...  ("+str(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))+")")
        # request.session['activity'] = temp_list
        ## request.session['activity']="Entered a "+request.session['building']+" and lost "+str(request.session['goldEarned'])+" gold... Ouch...  ("+str(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))+")\n"
    # return redirect('/')

# Easy way to reset our session data for testing
def destroy(request):
    request.session.clear()
    return redirect('/')