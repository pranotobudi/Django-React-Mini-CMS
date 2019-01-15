from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import ArticleSerializer, Article1Serializer, Article2Serializer
from articles.models import Article 
class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

from rest_framework.generics import ListAPIView
class Article1ListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = Article1Serializer 

from rest_framework.generics import ListAPIView
class Article2ListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = Article2Serializer
