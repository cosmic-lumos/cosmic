from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from . import models


# Create your views here.
def main(request):
    return redirect('root')


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        birthDate = request.POST['birthDateYear'] + '-' + request.POST['birthDateMonth'] + '-' + request.POST['birthDateDay']
        profile = models.Profile(user=user, name=request.POST['name'], birthDate=birthDate)

        user.save()
        profile.save()
        print('Sign Up Successed.')
        return redirect('account:main')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('Log In Successed.')
            return redirect('account:main')
        else:
            print('Log In Failed.\nWrong ID or Password.')
            return redirect('account:login')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        print('Log Out Successed.')
        return redirect('account:main')
    else:
        print('Log Out Failed.\nYou are not logged in.')
        return redirect('account:main')
