from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializer import UserSerializer, PollSerializer, VoteSerializer
from .models import Poll, Vote
User = get_user_model()

def main(request):
	return render(request, "main.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


def polls(request):
	return render(request, "vote.html")


@login_required(login_url='/login/')
def create(request):
	if request.method == "GET": # 투표생성 화면 띄워주기
		return render(request, "vote.html")
	elif request.method == "POST": # 투표생성 처리
		return redirect('index')


def login(request):
	if request.method == "GET": # 로그인 화면 띄워주기
		return render(request, "login.html")

	elif request.method == "POST": # 로그인 처리
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')

		user = authenticate(email=email, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return redirect('index')

		ctx = {'error': '회원 정보가 맞지 않습니다'}
		return render(request, "login.html", ctx)


def logout(request):
	auth_logout(request)
	return redirect('index')


def signup(request):
	if request.method == "GET": # 회원가입 화면 띄워주기
		return render(request, "signup.html")
	elif request.method == "POST": # 회원가입 처리
		data = request.POST.dict()
		del data['csrfmiddlewaretoken']
		print(data)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		else:
			print(serializer.errors)
			return HttpResponse(status=400)


@login_required(login_url='/login/')
def mypage(request):
	return render(request, "mypage.html")


@login_required(login_url='/login/')
def vote(request):
	return render(request, "vote.html")


@login_required(login_url='/login/')
def tables(request):
	return render(request, "tables.html")


@login_required(login_url='/login/')
def findpw(request):
	return render(request, "findpw.html")


def makeVote(request):
	return render(request, "makeVote.html")

@login_required(login_url='/login/')
def vote_specifications(request):
	return render(request, "vote_specifications.html")

def sendEmail(request):
	title = ''
	content = ''
	receiver = ''
	email = EmailMessage(title, content, to=[receiver])
	email.send()