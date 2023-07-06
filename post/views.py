from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializer import PostSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .filters import PostFilterSet
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_class = PostFilterSet

    @method_decorator(cache_page(60))  # Cache for 60 seconds
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
