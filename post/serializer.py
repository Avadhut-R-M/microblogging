from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    class Meta:
        model = Post
        fields = ("id","created", "updated", "user", "title", "content")
        read_only_fields = ("id",)