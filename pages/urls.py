from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.base import RedirectView
from .form import LoginForm, ResetPasswordForm

from .views import (
    home_view,
    contact_view,
    us_view,
    event_detail_view,
    event_list_view,
    members_join_view,
    information_view,
    signup_view,
    profile_view,
)


app_name = 'pages'
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about-us/', us_view, name='about_us'),
    path('events/', event_list_view, name='event'),
    path('event/<slug:slug>', event_detail_view, name='event-detail'),
    path('members/', members_join_view, name='members'),
    path('information/', information_view, name='information'),
    path('accounts/signup', signup_view, name="signup"),
    path('accounts/', profile_view, name='profile'),
    path('accounts/login/',
         views.LoginView.as_view(template_name='registration/login.html',
         form_class=LoginForm), name='login'),
    path('accounts/password_reset/',
         views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
         form_class=ResetPasswordForm), name='password_reset'),
]