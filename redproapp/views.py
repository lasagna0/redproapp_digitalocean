from django.shortcuts import render
#login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html', {})
def login(request):
    return render(request, 'login.html', {})

    
