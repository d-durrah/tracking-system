from django.urls import path, include

from user_manual import views

app_name = 'user_manual'
urlpatterns = [
    path('', views.home, name='home'),
    path('ios/', views.ios_manual, name='ios_manual'),
    path('android/', views.android_manual, name='android_manual'),
    path('windows/', views.windows_manual, name='windows_manual')
]
