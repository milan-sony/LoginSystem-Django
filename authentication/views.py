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

    if pass1 == pass2:
      if User.objects.filter(username=uname).exists():
        messages.warning(request,"Username Already Exist")
      elif User.objects.filter(email=email).exists():
        messages.warning(request,"Email Already Exist")
      else:
        user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
        user.save()
        messages.success(request,"Your Account Has been Successfully Created")
        return redirect('signup')
    else:
      messages.warning(request,"Password Is Not Matching")
  return render(request,"signup.html")

#signin page
# def login(request):
  # if request.method == 'POST':
    # uname = request.POST['uname']
    # pass1 = request.POST['pass1']

    # User = authenticate(uname = uname, pass1 = pass1)

    # if User is not None:
      # login(request, User)
      # return render(request,"userhomepage.html")
    # else:
      # messages.error(request,"Your Credentials Doesn't Match")
      # return redirect('login')

  # return render(request,"login.html")