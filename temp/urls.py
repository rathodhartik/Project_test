
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('base1', views.base1, name='base1'),
    path('home', views.home, name='home'),
    

]
