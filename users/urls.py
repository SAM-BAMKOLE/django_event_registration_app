from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.login_view, name='login_page'),
    path('auth/register/', views.register, name='register_page'),
    path('auth/logout/', views.logout_view, name='logout_view'),
]