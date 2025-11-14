from django.urls import path
from . import views

urlpatterns = [
    path('list_authors/', views.AuthorListApiView.as_view(), name='author_list'),
    path('detail_authors/<int:id>/', views.AuthorDetailApiView.as_view(), name='author_detail'),
    path('list_books/', views.BookListApiView.as_view(), name='book_list'),
    path('detail_books/<int:id>/', views.BookDetailApiView.as_view(), name='book_detail'),
    path('list_articles/', views.ArticleListApiView.as_view(), name='article_list'),
    path('detail_articles/<int:id>/', views.ArticleDetailApiView.as_view(), name='article_detail'),
]