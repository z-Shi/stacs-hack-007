from django.urls import path
from code_green.views import IndexView, RegisterProfileView, ProfileView, MissionsView

app_name = 'code_green'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register_profile/', RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path('missions/', MissionsView.as_view(), name='missions'),
    path('about/', IndexView.as_view(), name='about'),
    path('leaderboard/', IndexView.as_view(), name='leaderboard'),
    path('community/', IndexView.as_view(), name='community'),
]
