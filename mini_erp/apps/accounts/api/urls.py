from django.urls import path
from .views import RegisterView, LoginView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/me/', UserProfileView.as_view(), name='auth_me'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
