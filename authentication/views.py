from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
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

    if pass1 == pass2:
      if User.objects.filter(username=uname).exists():
        messages.warning(request,"Username Already Exist")
        return redirect('signup')
      elif User.objects.filter(email=email).exists():
        messages.warning(request,"Email Already Exist")
        return redirect('signup')
      else:
        user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
        user.save()
        messages.success(request,"Your Account Has been Successfully Created")
        return redirect('login')
    else:
      messages.warning(request,"Password Is Not Matching")
      return redirect('signup')
  return render(request,"signup.html")

#Login page
def login(request):
  if request.method == 'POST':
    uname = request.POST['uname']
    password = request.POST['password']
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/
    user = auth.authenticate(username=uname,password=password) 
    if user is not None:
      auth.login(request,user)
      return render(request,"userhomepage.html")
    else:
      messages.warning(request,"Invalid Credentials")
      return redirect('login')
  else:
    return render(request,"login.html")

#logout
def logout(request):
  auth.logout(request)
  return redirect('/')