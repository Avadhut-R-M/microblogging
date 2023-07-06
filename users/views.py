from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserSerializer, UserDetailSerializer, UserFollowSerializer
from rest_framework import viewsets, mixins
from .models import UserFollow
from post.serializer import PostSerializer
from post.models import PostLike, Post


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    This viewset is for user model
    This viewset supports create, update, retrive methods only.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]


    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        if self.action == "add_follower":
            return UserFollowSerializer
        return UserSerializer

    @action(methods=["GET"], detail=True)
    def add_follower(self, request, pk):
        follower = request.query_params.get("follower", None)
        serializer = self.get_serializer(data={"follower": follower, "following": pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Following": serializer.data})
    
    @action(methods=["GET"], detail=True)
    def list_follower(self, request, pk):
        following_users = User.objects.filter(
            id__in=UserFollow.objects.filter(follower_id=pk).values('following')
        )
        serializer = UserSerializer(following_users, many=True)
        return Response(serializer.data)
    
    @action(methods=["GET"], detail=True)
    def list_following(self, request, pk):
        following = User.objects.filter(
            id__in=UserFollow.objects.filter(following_id=pk).values('follower')
        )
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)
    
    @action(methods=["GET"], detail=True)
    def list_liked_posts(self, request, pk):
        liked_posts = Post.objects.filter(
            id__in=PostLike.objects.filter(user_id=pk).values('post')
        )
        serializer = PostSerializer(liked_posts, many=True)
        return Response(serializer.data)
