from django.urls import path, include
from members.views import members_join_view
from django.conf.urls import url

app_name = 'members'
urlpatterns = [
    path('', members_join_view, name='members'),
]