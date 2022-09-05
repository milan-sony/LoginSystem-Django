from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

#indexpage/homepage
def home(request):
  return render(request,"index.html")

#signup page
def signup(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    myusers = User.objects.create_user(uname, email, pass1)
    myusers.first_name = fname
    myusers.last_name = lname

    myusers.save()
    messages.success(request,"Your Account Has been Successfully Created")
    return redirect('signup')

  return render(request,"signup.html")

#signin page
def login(request):
  return render(request,"login.html")