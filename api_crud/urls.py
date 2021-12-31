
from django.urls import path
from .import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    #CRUD API
    #path('student_detail/', views.student_detail, name='student_detail'),
    path('student_detail/', views.student_list.as_view(),name='student_detail'),
    path('student_detail/<int:pk>/', views.student_detail.as_view()),
  



     # # Authentication Token
    path('create_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
