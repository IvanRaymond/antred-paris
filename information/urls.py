from django.urls import path, include
from information.views import information_view
from django.conf.urls import url

app_name = 'information'
urlpatterns = [
    path('', information_view, name='information'),
]