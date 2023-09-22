from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from  django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect

def auth(request):
    return render(request, "authentication/auth-home.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            request.session['current_user'] = user.id
            username = user.username
            messages.success(request, f"You are successfully logged in as {username}")
            return redirect('home')
        
        else:
            messages.error(request, "You entered bad credentials!!")
    return render(request, "authentication/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 != password2:
            messages.error(request,"passwords does not match")
        newUser = User.objects.create_user(username,email, password1)
        newUser.first_name = firstname
        newUser.last_name = lastname      

        newUser.save()
        login(request, newUser)
        request.session['current_user'] = newUser.id
        messages.success(request, "your account has been created successfully")
        return redirect('/auth/signin')
    return render(request, "authentication/signup.html")

def signout(request):
    logout(request)
    # try:
    #     del request.session['current_user']
    # except KeyError:
    #     pass
         
    messages.success(request, "you are logged out successfully")
    return redirect('home')

