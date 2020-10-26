from django.urls import path, include
from alumni.views import home_view
from django.conf.urls import url

app_name = 'alumni'
urlpatterns = [
    path('', home_view, name='alumni'),
]