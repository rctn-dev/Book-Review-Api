from BookBlogApp.api.serializers import BookSerializer, CommentSerializer
from BookBlogApp.models import Book, Comment
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from BookBlogApp.api.permissions import IsAdminOrReadOnly, IsOwner
from rest_framework.exceptions import ValidationError
from BookBlogApp.api.pagination import SmallNumberPagination, LargeNumberPagination

class BookView(generics.ListCreateAPIView):
    queryset=Book.objects.all().order_by('-id')
    serializer_class=BookSerializer
    permission_classes=[IsAdminOrReadOnly]
    pagination_class=LargeNumberPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes=[IsAdminOrReadOnly]

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
     
    # The specific book object determined by the URL is saved into book field
    # of the Comment serializer with perform_create method
    def perform_create(self, serializer):
        # path('book-view/<int:pk>/comment/',views.CommentCreateView.as_view(),name='comment-create'),
        # self.kwargs is used to retrieve the pk from the URL
        book_pk = self.kwargs.get('pk')
        book= get_object_or_404(Book, pk=book_pk)
        user=self.request.user
        # we have  to prevent multiple comments for the same book coming from the same user.
        previous_comment=Comment.objects.filter(book=book, user=user)
        if previous_comment.exists():
            raise ValidationError('A user can comment once for each book.')
        serializer.save(book=book, user=user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes=[IsOwner]
