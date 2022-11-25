from django.urls import path, include  # noqa
from rest_framework import routers
from .views import ArticleViewSets

router = routers.DefaultRouter()
router.register('articles', ArticleViewSets)

urlpatterns = router.urls
