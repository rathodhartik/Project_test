
from django.urls import path
from .import views




urlpatterns = [
    #CRUD Forms
    path('studentdetails', views.studentdetails, name='studentdetails'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('delete/<int:id>/', views.delete, name='delete'),

    #Searching Data in Forms
    path('search', views.search, name='search'),
]
