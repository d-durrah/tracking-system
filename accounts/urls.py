from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('password-reset/',
         PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),

]