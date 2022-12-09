from rest_framework import serializers
from .models import Category, Tag, Article, Comment
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    created_user = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'parent', 'title', 'description', )

        extra_kwargs = {
            'created_at': {
                'read_only': True,
                'required': False
            }
        }


class TagSerializer(serializers.ModelSerializer):
    created_user = UserSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'title', 'description', )

        extra_kwargs = {
            'created_at': {
                'read_only': True,
                'required': False
            }
        }


class CommentSerializer(serializers.ModelSerializer):
    created_user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', )

        extra_kwargs = {
            'created_at': {
                'read_only': True,
                'required': False
            }
        }


class ArticleSerializer(serializers.ModelSerializer):
    created_user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'description', 'created_user', 'created_at'
        )

        extra_kwargs = {
            'created_at': {
                'read_only': True,
                'required': False
            }
        }
