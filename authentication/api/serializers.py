from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Nested User Serializer 
class UserInfoDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] # fields to show for a particular author


# User Model Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}