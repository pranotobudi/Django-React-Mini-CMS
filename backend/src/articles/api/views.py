from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
) 

from .serializer import ArticleSerializer
from articles.models import Article 


class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class Article1ListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer 

# class Article2ListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
