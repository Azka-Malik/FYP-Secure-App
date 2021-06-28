from django.http import HttpResponse
from sklearn.cluster import KMeans
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from secureapp import settings
from django.shortcuts import render
from .models import RequestApi


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            user = auth.authenticate(
                username=request.POST['uname'], password=request.POST['pass'])
            if user is not None:
                    user123 = auth.login(request, user)
                    acceptedRequests = RequestApi.objects.filter(apiRequestStatus='Accept')
                    print(request.user.is_superuser)
                    return render(request, 'Home.html',{'isAdmin':request.user.is_superuser,'ApiRequests': acceptedRequests})

            else:
               return render(request, 'Login.html', {'error': "Invalid Login credentials"})
        else:
            return render(request, 'Login.html')

def logoutUser(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/')
def home(request):
    acceptedRequests = RequestApi.objects.filter(apiRequestStatus='Accept')
    if request.method == "POST":
        nam = request.POST['nam']
        mail = request.POST['mail']
        num = request.POST['num']
        nic = request.POST['nic']
        response = RequestApi(name=nam, email=mail,phoneNumber=num,cnic=nic)
        response.save()
        print('Requested')
        return render(request, 'Home.html', {'isAdmin':request.user.is_superuser,'ApiRequests': acceptedRequests,'SRnam':nam,'SRmail':mail,'SRnum':num,'SRnic':nic })

    return render(request, 'Home.html',{'isAdmin':request.user.is_superuser,'ApiRequests': acceptedRequests})

def create(request):
    print('SHIT')
    if request.method == "POST":
        if request.POST['pass'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'Login.html', {'error': "Username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(
                   username=request.POST['username'], password=request.POST['pass'],first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],is_superuser=0)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'Login.html', {'error': "Password Don't Match"})
    else:
        return render(request, 'Login.html')
   

def AdminReq(request):
    print(str(request.user.is_superuser)+ 'WOW')
    acceptedRequests = RequestApi.objects.filter(apiRequestStatus='Accept')
    pendingRequests = RequestApi.objects.filter(apiRequestStatus='pending')
    context = {'ApiRequests': pendingRequests,'isAdmin':request.user.is_superuser}
    if request.method == "POST":
        print(request.POST.get('work', None))
        upd = RequestApi.objects.filter(id= request.POST.get('work', None))
        upd.update(apiRequestStatus=request.POST.get('status', None))
        return render(request, 'Home.html',{'ApiRequests': acceptedRequests,'isAdmin':request.user.is_superuser})

    return render(request, 'AdminRequest.html',context)


