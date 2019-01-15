from django.urls import path

from .views import ArticleListView, ArticleDetailView, Article1ListView, Article2ListView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('article1/', Article1ListView.as_view()),
    path('article2/', Article2ListView.as_view()),
    path('<pk>', ArticleDetailView.as_view())
    
]