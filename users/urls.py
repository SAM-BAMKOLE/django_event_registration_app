from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('register/', views.register, name='register_page'),
    path('logout/', views.logout_view, name='logout_view'),
    path('registered-events/', views.registered_events, name='account_registrations'),
]