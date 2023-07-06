from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, User, PostLike
from .serializer import PostSerializer, PostDetailSerializer, PostLikeSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .filters import PostFilterSet
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializer import UserSerializer
from django.http import Http404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_class = PostFilterSet

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        if self.action == "like_post":
            return PostLikeSerializer
        return PostSerializer

    @method_decorator(cache_page(60))  # Cache for 60 seconds
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(methods=["GET"], detail=True)
    def like_post(self, request, pk):
        user = request.query_params.get("user", None)
        like = request.query_params.get("like", True)
        if user and PostLike.objects.filter(user=user, post=pk).count():
            if like == "false":
                postlike = PostLike.objects.filter(user=user, post=pk, like=True).last()
                if postlike:
                    postlike.like = False
                    postlike.save()
                    return Response({"Data": "Post Disliked"})
                else:
                    raise Http404

            if like == "true" or like:
                postlike = PostLike.objects.filter(
                    user=user, post=pk, like=False
                ).last()
                if postlike:
                    postlike.like = True
                    postlike.save()
                    return Response({"Data": "Post Liked"})
                else:
                    raise Http404
        serializer = self.get_serializer(data={"user": user, "post": pk, "like": like})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Data": "Post Liked"})

    @action(methods=["GET"], detail=True)
    def list_liked_by(self, request, pk):
        liked_by = User.objects.filter(
            id__in=PostLike.objects.filter(post_id=pk).values("user")
        )
        serializer = UserSerializer(liked_by, many=True)
        return Response(serializer.data)
