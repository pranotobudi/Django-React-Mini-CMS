from rest_framework import serializers 
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']

# class Article1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ['title', 'content']

# class Article2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article 
#         fields = ['title', 'content']