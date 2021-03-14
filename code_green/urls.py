from django.urls import path
from code_green.views import IndexView, RegisterProfileView, ProfileView, MissionsView, AboutView, LeaderboardView, \
    CommunityView

app_name = 'code_green'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register_profile/', RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path('missions/', MissionsView.as_view(), name='missions'),
    path('about/', AboutView.as_view(), name='about'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('community/', CommunityView.as_view(), name='community'),
]
