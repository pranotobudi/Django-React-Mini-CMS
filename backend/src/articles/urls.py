from django.urls import path
from .views import ArticleListView, Article1ListView, Article2ListView, Article3ListView, Article4ListView, Article5ListView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('article1', Article1ListView.as_view(), name='article1'),
    path('article2', Article2ListView.as_view(), name='article2'),
    path('article2', Article2ListView.as_view(), name='article2'),
    path('article3', Article3ListView.as_view(), name='article3'),
    path('article4', Article4ListView.as_view(), name='article4'),
    path('article5', Article5ListView.as_view(), name='article5'),
]