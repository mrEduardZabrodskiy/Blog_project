from django.shortcuts import render, redirect
from .models import Profile
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                username = cd['username']
                password = cd['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse('dashboard'))
        elif request.method == 'GET':
            login_form = LoginForm()
            register_form = RegistrationForm()
            return render(request, 'login.html', {
                'login_form': login_form,
                'register_form': register_form})

def logout_view(request):
    logout(request)
    return redirect(reverse('login_view'))
    

def registration_view(request):
    if request.user.is_authenticated:
        pass
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.create_user(
                    username = cd['username'],
                    password = cd['password'],
                    email = cd['email']
                )
                user.save()
                Profile.objects.create(user=user)
                return HttpResponse('User is created')
            else:
                return HttpResponse('Some data is wrong')
        elif request.method == 'GET':
            form = RegistrationForm()
            return render(request, 'registration.html', {'form': form})
        


