from django.urls import path
from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

# from .views import (
#     ArticleListView, 
#     ArticleDetailView, 
#     Article1ListView, 
#     Article2ListView, 
#     ArticleCreateView,
#     ArticleUpdateView,
#     ArticleDeleteView,
#     )

# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('article1/', Article1ListView.as_view()),
#     path('article2/', Article2ListView.as_view()),
#     path('<pk>/update/', ArticleUpdateView.as_view()),
#     path('<pk>/delete/', ArticleDeleteView.as_view()),
#     path('<pk>/', ArticleDetailView.as_view()),
# ]

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')
urlpatterns = router.urls
