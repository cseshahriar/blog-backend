from django.urls import path, include  # noqa
from rest_framework import routers
from .views import (
    CategoryViewSets, TagViewSets, CommentViewSets, ArticleViewSets
)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSets)
router.register('tags', TagViewSets)
router.register('comments', CommentViewSets)
router.register('articles', ArticleViewSets)

urlpatterns = router.urls
