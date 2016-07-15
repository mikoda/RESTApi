from rest_framework import serializers

from Blog.models import Post

class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'created'
        ]

class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
        ]


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'author'
        ]