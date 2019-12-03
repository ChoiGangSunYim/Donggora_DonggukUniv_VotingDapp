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
    path('mypage', views.mypage, name='mypage'),
    path('findpw', views.findpw, name='findpw'),
    path('vote', views.vote, name='vote'),
    path('vote_specifications/<int:id>', views.vote_specifications, name='vote_specifications'),
    path('vote_proscons/<int:id>', views.vote_proscons, name='vote_proscons'),
    path('tables', views.tables, name='tables'),
    path('finished_specifications/<int:id>', views.finished_specifications, name='finished_specifications'),
    path('comment', views.comment, name='comment'),
]