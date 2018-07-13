from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    return render(request,'ninja_gold_app/index.html')