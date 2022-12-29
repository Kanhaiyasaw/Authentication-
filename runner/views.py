from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User # import in-built User models
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from runner.models import User_address # import user difine models
from django.contrib.auth.decorators import login_required # import login_required in-built function

# In-built function of django for without login user can't log in in the system
@login_required(login_url='login')
# specific user home page if authentic user exists in the database 
def home(request):
    return render(request, 'home.html') 

# signup Opration Praforming here
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:#check Comparision of both password 
            # User table Insertion Opration
            # create_user() that use for create the user in side of admin panel User Table 
            user_in = User.objects.create_user(username, email, password)# it only consider 3 argument
            user_in.first_name = first_name
            user_in.last_name = last_name
            user_in.save()
            # user difine models insert opration
            user_add = {
                'address' : address,
                'city' : city
            }
            User_address.objects.create(user = user_in, **user_add)#inserting the data in the table by Foriegn key with User Table
            return redirect('login')
        else:
            # If not password match then it will give error
            return HttpResponse('Password does not match')
    return render(request, 'signup.html')

# Login Opreation 
def login_page(request):
    if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                # authenticate() is verify the user are existing or not 
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # login() is used for if user authenticate then it will redirect to home page
                    login(request, user)
                    return redirect('home')
                else:
                    # otherwise it will give error 
                    return redirect('login')    
    return render(request, 'index.html')

# logout Opration performing 
def logout_page(request):
    logout(request)# logout() is used for logout the user to the home page of system
    return redirect('login')

# That function is used for change the password during user login 
def change_pass(request):
    if request.method == "POST":
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        u = User.objects.get(username=request.user.username)# it will fetch the Username from User Table 
        if new_password == confirm_password:# comparision
            u.set_password(new_password)# set_password() set the password in the database 
            u.save()
            update_session_auth_hash(request, u)# it will not destroy the session after the changing password
            return redirect('home')
        else:
            return HttpResponse('Password not Match')
    return render(request, 'home.html')