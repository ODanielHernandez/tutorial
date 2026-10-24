from django.urls import path, include
from rest_framework import routers

from .views import get_user, get_users, create_user, user_detail, StudentViewSet, ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"students", StudentViewSet, "student")
router.register(r"products", ProductViewSet, "product")
router.register(r"categories", CategoryViewSet, "category")

urlpatterns = [
    path("", include(router.urls)),
    path("user/", get_user, name="get_user"),
    path("users/", get_users, name="get_users"),
    path("create_user/", create_user, name="create_user"),
    path("users/<int:pk>/", user_detail, name="user_detail"),
]
