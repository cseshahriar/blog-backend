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
    created_user = UserSerializer(read_only=True)  # m2o
    tags = TagSerializer(many=True, read_only=True)  # m2m

    class Meta:
        model = Article
        fields = (
            'id', 'category', 'title', 'description', 'meta_keywords',
            'thumbnail', 'status', 'created_user', 'created_at', 'published_at'
        )

        extra_kwargs = {
            'created_at': {
                'read_only': True,
                'required': False
            },
            'published_at': {
                'read_only': True,
                'required': False
            },
            'tags': {'required': False},
        }
