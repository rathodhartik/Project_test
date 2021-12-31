
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Register ,Login,Chenge Password , Logout
    path('register', views.register, name='register'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('chengpwd', views.chengpwd, name='chengpwd'),
    

]
