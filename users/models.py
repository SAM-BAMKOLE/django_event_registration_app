from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# Create your models here.

class RegisterForm(UserCreationForm):
    """Form to Create new User"""
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]
