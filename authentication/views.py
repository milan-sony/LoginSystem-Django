from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# https://stackoverflow.com/questions/39316948/typeerror-login-takes-1-positional-argument-but-2-were-given
# Your view has the same name as the auth login function, so it is hiding it. Change the view name, or import the function under a different name eg from django.contrib.auth import login as auth_login.
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib import messages

# Create your views here.

#indexpage/homepage
def home(request):
  return render(request, "index.html")

# We are using djangos default user model 
# https://docs.djangoproject.com/en/4.1/topics/auth/default/

#signup page
def signup(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    if pass1 == pass2:
      if User.objects.filter(username=uname).exists():
        messages.warning(request, "Username Already Exist")
        return redirect('signup')
      elif User.objects.filter(email=email).exists():
        messages.warning(request, "Email Already Exist")
        return redirect('signup')
      else:
        user = User.objects.create_user(username=uname ,first_name=fname, last_name=lname, email=email, password=pass1)
        user.save()
        messages.success(request,"Your Account Has been Successfully Created")
        return redirect('login')
    else:
      messages.warning(request, "Password Is Not Matching")
      return redirect('signup')
  return render(request,"signup.html")

#Login page
def login(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    password = request.POST['password']
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.authenticate
    # Use authenticate() to verify a set of credentials. It takes credentials as keyword arguments, username and password for the default case, checks them against each authentication backend, and returns a User object if the credentials are valid for a backend. If the credentials aren’t valid for any backend or if a backend raises PermissionDenied, it returns None.
    user = authenticate(request, username=uname, password=password) 
    if user is not None:
      auth_login(request, user)
      return render(request, "userhomepage.html")
    else:
      messages.warning(request, "Check Your Username and Password")
      return redirect('login')
  else:
    return render(request, "login.html")

#logout
def logout(request):
  logout(request)
  return redirect('/')