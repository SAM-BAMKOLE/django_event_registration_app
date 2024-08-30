from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.add_registration, name="register_event"),
]