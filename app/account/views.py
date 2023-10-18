from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from .forms import *


# Create your views here.

def login_func(request):
    if request.user.is_authenticated:
        return redirect("index")
    context = {}

    if request.method == 'POST':
        print("post")
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            print("valid")
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            login(request, user)
            # request.session.set_expiry(2000)

            return redirect('index')

    else:
        form = LoginForm()
    context["form"] = form
    return render(request,"login.html",context)


def logout_view(request):

    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    context = {}

    if request.method == 'POST':
        print("I am in first if")
        form = RegisterForm(request.POST)

        if form.is_valid():
            print("I am in valid")
            user = form.save(commit=False)

            user.save()
            return redirect("login")
          
    else:
        form = RegisterForm()


    context["form"] = form


    return render(request,"register.html",context)
