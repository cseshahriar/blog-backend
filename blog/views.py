from rest_framework import viewsets
from .models import Category, Tag, Article, Comment
from .serializers import (
    CategorySerializer, TagSerializer, CommentSerializer, ArticleSerializer
)
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_user=self.request.user)


class TagViewSets(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_user=self.request.user)


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment().objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_user=self.request.user)


class ArticleViewSets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_user=self.request.user)
