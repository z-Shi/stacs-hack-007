from django.urls import path
from code_green.views import IndexView

app_name = 'code_green'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
