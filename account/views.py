from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Account
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return redirect('signin')


def register(request):
    if request.method == 'GET':
        return render(request, "pages/register.html")
    else:
        email = request.POST['email']
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        contact = request.POST['contact']
        if(pass1 == pass2):
            a = Account(email=email, contact_no=contact)
            a.set_password(pass1)
            a.save()
            return redirect('signin')
        else:
            return redirect('signup')


@login_required(login_url='signin')
def account(request):
    return render(request, "pages/profile.html")


def signout(request):
    logout(request)
    return redirect('signin')
