from rest_framework import routers
from django.urls import path,include
from . import views
from .views import UserViewSet, PollViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'poll', PollViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('polls/', views.polls, name='polls'),
    path('create/', views.create, name='create'),
    path('mypage', views.mypage, name='mypage'),
    path('vote', views.vote, name='vote'),
    path('findpw', views.findpw, name='findpw'),
    path('tables', views.tables, name='tables'),
    path('makeVote', views.makeVote, name='makeVote'),
]