from rest_framework import serializers
from .models import Category, Tag, Article, Comment
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    created_user = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'parent', 'title', 'description', 'created_user')

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
        fields = ('id', 'title', 'description', 'created_user', )

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
        fields = ('id', 'content', 'created_user', )

        extra_kwargs = {
            'created_at': {
                'read_only': True,
                'required': False
            }
        }


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 'category', 'tags', 'title', 'description', 'meta_keywords',
            'thumbnail', 'status', 'created_user', 'created_at', 'published_at'
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        # foreignKey
        response['created_user'] = UserSerializer(instance.created_user).data
        # m2m
        response['tags'] = TagSerializer(instance.tags, many=True).data
        return response
