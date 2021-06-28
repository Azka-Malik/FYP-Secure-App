from django.http import HttpResponse
from sklearn.cluster import KMeans
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from secureapp import settings
from django.shortcuts import render

def Clientlogin(request):
    if request.user.is_authenticated:
        return redirect('CLhome')
    else:
        if request.method == "POST":
            user = auth.authenticate(
                username=request.POST['uname'], password=request.POST['pass'])
            if user is not None and user.is_active is not 0:
                auth.login(request, user)
                return redirect('CLhome')
            else:
                return render(request, 'Clientlogin.html', {'error': "LOGIN FAILED"})
        else:
            return render(request, 'Clientlogin.html')
def Clientlogout(request):
    auth.logout(request)
    return redirect('/Clientlogin')

@login_required(login_url='/Clientlogin')
def CLhome(request):
    return render(request, 'CLhome.html')

def ClientCreate(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'Clientlogin.html', {'error': "Username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(
                   username=request.POST['username'], password=request.POST['pass'],first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],is_superuser=0)
                auth.login(request, user)
                return redirect('question')
        else:
            return render(request, 'Clientlogin.html', {'error': "Password Don't Match"})
    else:
        return render(request, 'Clientlogin.html')

