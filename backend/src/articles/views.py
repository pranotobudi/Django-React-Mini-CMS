from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, Article1, Article2, Article3, Article4
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class Article1ListView(ListView):
    model = Article1
    template_name = 'article1_list.html'

class Article2ListView(ListView):
    model = Article2
    template_name = 'article2_list.html'

class Article3ListView(ListView):
    model = Article3
    template_name = 'article3_list.html'

class Article4ListView(ListView):
    model = Article4 
    template_name = 'article4_list.html'

class Article5ListView(ListView):
    model = Article4 
    template_name = 'article5_list.html'
