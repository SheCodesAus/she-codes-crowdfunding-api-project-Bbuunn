from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(
        max_length=200
        # style={'input_type': 'password'}
    )

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

class CustomUserDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
