from rest_framework import serializers

from .models import Tag, Category, Article, Comment


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Comment
        fields = '__all__'

