from django.urls import path
from . import views


urlpatterns = [
  # /
  path('', views.home, name='home'),
  path('signin', views.sign_in, name='signin'),
  path('calendar', views.calendar, name='calendar'),
  path('alert', views.alert, name='alert'),
  path('callback', views.callback, name='callback'),
  path('signout', views.sign_out, name='signout'),
]
