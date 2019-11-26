from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializer import UserSerializer, PollSerializer, VoteSerializer, CommentSerializer
from .models import Poll, Vote, Comment
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

index = 0

@login_required(login_url='/login/')
def vote(request):
	if request.method == "GET": # 투표생성 화면 띄워주기
		return render(request, "vote.html")
	elif request.method == "POST": # 투표생성 처리
		data = request.POST.dict()
		del data['csrfmiddlewaretoken']
		data['valid_until'] = data['year'] + '-' + data['month'] + '-' + data['day']
		del data['year']
		del data['month']
		del data['day']

		print(data)
		serializer = PollSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return redirect('main')
		else:
			print(serializer.errors)
			return HttpResponse(status=400)

		# id = request.POST.get('id', '')
		# url = '\n 투표에 참여하시려면 클릭하세요 => ' + f'http://localhost:8000/vote_specifications/{id}'
		# content+=url

		# array = []
		# array[index]
		# index+=1
		
		# def _sendEmail(title, content):
		# 	email = EmailMessage(title, content, to=['donggoracontact@gmail.com'])
		# 	email.send()

		# _sendEmail(title, content)

		return redirect('main')


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
				return redirect('main')

		ctx = {'error': '회원 정보가 맞지 않습니다'}
		return render(request, "login.html", ctx)


def logout(request):
	auth_logout(request)
	return redirect('main')


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
			return redirect('main')
		else:
			print(serializer.errors)
			return HttpResponse(status=400)


@login_required(login_url='/login/')
def mypage(request):
	return render(request, "mypage.html")


@login_required(login_url='/login/')
def tables(request):
	polls = Poll.objects.all()

	ctx = {
		'polls': polls
	}
	return render(request, "tables.html", ctx)


@login_required(login_url='/login/')
def findpw(request):
	if request.method == "GET": # 비번찾기 화면 띄워주기
		return render(request, "findpw.html")
	elif request.method == "POST": # 비밀번호 찾기
		data = request.POST.dict()
		del data['csrfmiddlewaretoken']
		print(data)
		email = data['email']
		user = User.objects.filter(email)
		if user:
			# todo
			return redirect('index')
		else:
			# todo
			return redirect('findpw')


@login_required(login_url='/login/')
def vote_specifications(request, id):
	poll = Poll.objects.filter(id=id)
	comments = Comment.objects.filter(poll=id)

	ctx = {
		'poll': poll,
		'comments': comments
	}

	return render(request, "vote_specifications.html", ctx)


@login_required(login_url='/login/')
def comment(request, poll_id):
	if request.method == 'POST':
		content = request.POST.get('content', '')
		data = request.POST.dict()
		del data['csrfmiddlewaretoken']
		data['poll'] = poll_id
		print(data)
		serializer = CommentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return redirect('vote_specifications')
		else:
			print(serializer.errors)
			return HttpResponse(status=400)
