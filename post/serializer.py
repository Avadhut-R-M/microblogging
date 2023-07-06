from rest_framework import serializers
from .models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    """
    Serilaizer for Post
    created, updated, id are readonly fields
    """

    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "created", "updated", "user", "title", "content")
        read_only_fields = ("id",)


class PostDetailSerializer(PostSerializer):
    post_likes = serializers.SerializerMethodField()

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ('post_likes',)

    def get_post_likes(self, instance):
        try:
            return instance.likes.count()
        except:
            return 0
        
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('user', 'post', 'like')