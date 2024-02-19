from rest_framework import serializers
from .models import (Category,
                     Tag,
                     Comment,
                     Subscribe,
                     Author,
                     Advertising,
                     Post,
                     InstagramImages)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class InstagramImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramImages
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only = ['created_at', 'updated_at']
