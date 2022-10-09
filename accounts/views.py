from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from shop.views import home

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password1 = request.POST['pass']
        password2 = request.POST['repass']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,username=username)
                user.save();
                print("succesfully registered")
                return redirect('/')
        else:
            return redirect('register')
        return redirect(home)
    else:
        return render(request,"register1.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

