__author__ = 'nisahu'
from rest_framework import serializers
from models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('created_at', 'title', 'slug', 'body')
