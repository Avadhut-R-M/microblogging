from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    # Other URL patterns
    path("", include(router.urls)),
]
