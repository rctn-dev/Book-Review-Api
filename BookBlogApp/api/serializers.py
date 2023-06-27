from rest_framework import serializers
from BookBlogApp.models import Book, Comment 


class CommentSerializer(serializers.ModelSerializer):
    # since the user will be handled within the views.py
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields='__all__'
        read_only_fields=['book']

class BookSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(read_only=True,many=True)
    class Meta:
        model=Book
        fields='__all__'

