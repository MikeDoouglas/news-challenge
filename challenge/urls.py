from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import (
    ArticleByCategoryView,
    ArticleDetailView,
    ArticleViewSet,
    AuthorViewSet,
)

router = routers.DefaultRouter()
router.register('admin/articles', ArticleViewSet)
router.register('admin/authors', AuthorViewSet)

urlpatterns = [
    path("", include(router.get_urls())),
    path("articles/<uuid:pk>", ArticleDetailView.as_view()),
    path("articles/", ArticleByCategoryView.as_view()),
]
