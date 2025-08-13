from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .api import (
    CustomTokenObtainPairView,
    UserConfirmView,
    UserDeleteView,
    UserProfileView,
    UserRegisterView,
    UserUpdateView,
)

app_name = 'users'  

urlpatterns = [
    # Auth endpoints
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('confirm/', UserConfirmView.as_view(), name='confirm'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Authenticated user endpoints
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('delete/', UserDeleteView.as_view(), name='delete'),
]