from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('login', views.login, name='login'),
    path('vote', views.vote, name='vote'),
    path('findpw', views.findpw, name='findpw'),
    path('tables', views.tables, name='tables'),
    path('signup', views.signup, name='signup'),
    path('mypage', views.mypage, name='mypage'),
    path('makeVote', views.makeVote, name='makeVote'),
]
