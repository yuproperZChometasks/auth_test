#authapp/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, ProfileView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='authapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
