from rest_framework import serializers
from .admin import Article
from users.serializers import UserSerializer


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
