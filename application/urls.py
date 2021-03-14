from django.contrib import admin
from django.urls import path, include, reverse
from registration.backends.simple.views import RegistrationView
from code_green.views import IndexView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('code_green:register_profile')


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('code_green/', include('code_green.urls')),
]
