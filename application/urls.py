from django.contrib import admin
from django.urls import path, include
from code_green.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('code_green/', include('code_green.urls')),
]
