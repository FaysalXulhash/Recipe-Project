from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register (request):
    if request.method == "POST":
        data = request.POST
        username = data.get('user_name')
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username Already Taken. Try another one!")
            return redirect('user-register')

        user = User.objects.create(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Successfully! You Can Now Log In!")
        return redirect ('user-register-success')
    return render (request, 'users/register.html')

def success(request):
    return render(request, 'users/success.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User doesn't exists!")
            return redirect('user-login')
        user = authenticate(username=username, password=password)
        if user is None:
          messages.error(request, "Invalid Username or Password")
          return redirect('user-login')
        else:
            login(request ,user)
            return redirect('recipe-home')  
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

    
