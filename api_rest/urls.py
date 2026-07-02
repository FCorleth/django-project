from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nickname>', views.get_users_by_nickaname),
    path('data/', views.user_manager)
]