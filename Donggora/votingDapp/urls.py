from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from .views import UserViewSet, PollViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'poll', PollViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('polls/', views.polls, name='polls'),
    path('create/', views.create, name='create'),
]