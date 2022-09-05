from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

#indexpage/homepage
def home(request):
  return render(request,"index.html")

#signup page
def signup(request):
  return render(request,"signup.html")

#signin page
def signin(request):
  return render(request,"signin.html")