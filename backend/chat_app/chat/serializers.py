from rest_framework import serializers
from .models import CustomUser
from django.forms import PasswordInput

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'full_name',
            'position',
            'date_of_birth',
            'phone_number',
            'mail',
            'social_media'
        ]

