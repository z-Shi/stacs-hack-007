from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from code_green.views import IndexView, RegisterProfileView, ProfileView

app_name = 'code_green'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register_profile/', RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
