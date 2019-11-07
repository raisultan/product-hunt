from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # if user wants to register now
        if request.POST['password'] == request.POST['password_confirm']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'User already exists'})
            except User.DoesNotExist:
                # creating a new user
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                # loggin in with new user
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # if user wants to see signup page
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        #user wants to login
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'No such user'})
    else:
        #user wants login page
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')