from rest_framework import serializers
from django.core import validators
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import Custom_user


class UserSerializer(serializers.ModelSerializer):
    # email=serializers.CharField(max_length=200,validators=[validators.EmailValidator(message="Invalid username")])
    class Meta:
        model=User
        fields=('username','password')