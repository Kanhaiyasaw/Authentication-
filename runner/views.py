from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from runner.models import User_address
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html') 


def signup(request):
    if request.method == "POST":
        fname = request.POST.get('txtfname')
        lname = request.POST.get('txtlname')
        uname = request.POST.get('txtuname')
        email = request.POST.get('txtemail')
        address = request.POST.get('txtadd')
        city = request.POST.get('txtcity')
        pwd1 = request.POST.get('txtpwd1')
        pwd2 = request.POST.get('txtpwd2')
        if pwd1 == pwd2:
            user_in = User.objects.create_user(uname, email, pwd1)
            user_in.first_name = fname
            user_in.last_name = lname
            user_in.save()
            user_add = {
                'address' : address,
                'city' : city
            }
            User_address.objects.create(user = user_in, **user_add)
            return redirect('index')
        else:
            return HttpResponse('Password does not match') 
    return render(request, 'signup.html')

def login_page(request):
    if request.method == "POST":
                username = request.POST.get('txtuname')
                pwd = request.POST.get('txtpwd')
                user = authenticate(request, username=username, password=pwd)
                if user is not None:
                    login(request, user)
                    print(user.username)
                    return redirect('home')
                else:
                    messages.info(request, 'You Username and Password is Wrong!')
                    return redirect('login')    
    return render(request, 'index.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def change_pass(request):
    if request.method == "POST":
        npwd = request.POST.get('pwd1')
        cnpwd = request.POST.get('pwd2')
        u = User.objects.get(username=request.user.username)
        if npwd == cnpwd:
            u.set_password(npwd)
            u.save()
            update_session_auth_hash(request, u)
            return redirect('home')
        else:
            return HttpResponse('Password not Match')
    return render(request, 'home.html')