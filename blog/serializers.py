from rest_framework import serializers
from users.serializers import UserSerializer
from .admin import Article


class ArticleSerializer(serializers.ModelSerializer):
    created_user = UserSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'description',
        )
