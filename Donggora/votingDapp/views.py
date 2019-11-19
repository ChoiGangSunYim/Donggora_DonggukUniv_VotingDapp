from django.shortcuts import render
# Create your views here.

def index(request):
	return render(request, "main.html")
def findpw(request):
	return render(request, "findpw.html")
def login(request):
	return render(request, "login.html")
def signup(request):
	return render(request, "signup.html")
def tables(request):
	return render(request, "tables.html")
def vote(request):
	return render(request, "vote.html")
def mypage(request):
	return render(request, "mypage.html")
