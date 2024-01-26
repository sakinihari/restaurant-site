from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User


# Create your views here.

def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist!!")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist!!")
                return redirect("registration")
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username,
                                                password=password)
                user.save()
            return redirect("/")
        else:
            messages.info(request, "Password Mismatch!!")
            return redirect("registration")
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid details!!")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
