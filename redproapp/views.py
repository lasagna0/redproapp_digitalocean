from django.shortcuts import render
#login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

## upload users with csv
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'index.html', {})
def login(request):
    return render(request, 'login.html', {})

@login_required
def probarranquilla(request):
    return render(request, 'asistentes/probarranquilla.html', {})

@login_required
def proantioquia(request):
    return render(request, 'asistentes/proantioquia.html', {})

@login_required
def probogota(request):
    return render(request, 'asistentes/probogota.html', {})

@login_required
def propacifico(request):
    return render(request, 'asistentes/propacifico.html', {})

@login_required
def prorisaralda(request):
    return render(request, 'asistentes/prorisaralda.html', {})

@login_required
def prosantamarta(request):
    return render(request, 'asistentes/prosantamarta.html', {})

@login_required
def prosantander (request):
    return render(request, 'asistentes/prosantander.html', {})

@login_required
def protolima(request):
    return render(request, 'asistentes/protolima.html', {})



from tablib import Dataset
from .resources import UserResource


# must be admin to upload users


from django.http import JsonResponse
from csv import reader
from django.contrib.auth.models import User

def userdata(request):
    # authenticate user and check if admin
    if request.user.is_authenticated:
        if request.user.is_superuser:
            with open('templates/csv/aa.csv', 'r') as csv_file:
                csv_reader = reader(csv_file)
                for row in csv_reader:
                    password = row[0]
                    username = row[1]
                    email = row[2]
                    user = User.objects.create_user(username, email)
                    user.set_password(password)
                    user.save()

                return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': 'not admin'})
    else:
        return JsonResponse({'message': 'not authenticated'})
    

