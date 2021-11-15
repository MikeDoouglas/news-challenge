from django.contrib.auth.models import User
from rest_framework import serializers

from challenge.models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleLoggedSerializer(ArticleSerializer):
    class Meta(ArticleSerializer.Meta):
        fields = ["id", "author", "category", "title",
                  "summary", "firstParagraph", "body"]


class ArticleAnonymousSerializer(ArticleSerializer):
    class Meta(ArticleSerializer.Meta):
        fields = ["id", "author", "category",
                  "title", "summary", "firstParagraph"]


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, user):
        return User.objects.create_user(user['username'], password=user['password'])
