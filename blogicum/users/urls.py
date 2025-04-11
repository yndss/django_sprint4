from django.urls import path, include
from .views import RegisterView, EditProfileView, ProfileDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_reset_form.html',
        success_url='/users/profile/'), name='password_change'),
    path('', include('django.contrib.auth.urls')),
]