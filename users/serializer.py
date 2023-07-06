from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import UserFollow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if "email" not in attrs:
            raise serializers.ValidationError("Email field is required.")
        return attrs

    def validate_email(self, value):
        # Check if the email is a valid email address
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email address")

        return value

    def validate_username(self, value):
        # Check if the username is unique
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")

        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username", None),
            email=validated_data.get("email", None),
            password=validated_data.get("password", None),
        )
        return user


class UserDetailSerializer(UserSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("followers_count", "following_count")

    def get_followers_count(self, instance):
        try:
            return instance.following.count()
        except Exception as e:
            print(e)
            return 0
        
    def get_following_count(self, instance):
        try:
            return instance.followers.count()
        except Exception as e:
            print(e)
            return 0

class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = ('follower', 'following')