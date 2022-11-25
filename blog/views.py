from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.authentication import TokenAuthentication


class ArticleViewSets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication, ]
