from django.urls import path
from BookBlogApp.api import views

urlpatterns = [
    path('book-view/',views.BookView.as_view(),name='book-view'),
    path('book-view/<int:pk>/',views.BookDetailView.as_view(),name='book-detail'),
    path('comment-view/<int:pk>/',views.CommentDetailView.as_view(),name='comment-detail'),
    path('book-view/<int:pk>/comment/',views.CommentCreateView.as_view(),name='comment-create'),
]