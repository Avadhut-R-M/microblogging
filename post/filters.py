import django_filters
from .models import Post


class PostFilterSet(django_filters.FilterSet):
    """
    filter set for postviewset
    """

    user_id = django_filters.CharFilter(field_name="user_id")

    class Meta:
        model = Post
        fields = [
            "user_id",
        ]
