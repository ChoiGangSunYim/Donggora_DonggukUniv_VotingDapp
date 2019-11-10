from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializer import UserSerializer, PollSerializer, VoteSerializer
from .models import Poll, Vote
User = get_user_model()

def index(request):
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

		return redirect('index')


def signup(request):
	if request.method == "GET": # 회원가입 화면 띄워주기
		return render(request, "signup.html")
	elif request.method == "POST": # 회원가입 처리
		data = request.POST.dict()
		del data['csrfmiddlewaretoken']
		print("111111")
		print(data)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return redirect('index')
		else:
			print(serializer.errors)
			return HttpResponse(status=400)