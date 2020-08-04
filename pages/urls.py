from django.urls import path, include
from django.conf.urls import url
from .views import (
    home_view,
    contact_view,
    us_view
)

app_name = 'pages'
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about-us/', us_view, name='about_us')
]