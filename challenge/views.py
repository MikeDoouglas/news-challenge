from django.contrib.auth.models import User
from django.http.response import Http404
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.exceptions import ErrorDetail, ValidationError, NotFound


from challenge.models import Article, Author
from challenge.serializers import ArticleAnonymousSerializer, ArticleLoggedSerializer, ArticleSerializer, AuthorSerializer, SignUpSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class ArticleByCategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        category = request.query_params.get("category", None)
        article = Article.objects.filter(category=category).all()
        serializer = ArticleSerializer(instance=article, many=True)
        return Response(data=serializer.data)


class ArticleDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

        if request.user.is_authenticated:
            serializer = ArticleLoggedSerializer(article)
        else:
            serializer = ArticleAnonymousSerializer(article)
        return Response(serializer.data)
