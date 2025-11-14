from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, Book, Article
from .serializer import AuthorSerializer, BookSerializer, ArticleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class AuthorListApiView(APIView):
    
    def get(self, request):
        authors = Author.objects.all()
        ser = AuthorSerializer(authors, many=True)
        return Response(ser.data,  status=status.HTTP_200_OK)
    
    def post(self, request):
        ser = AuthorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthorDetailApiView(APIView):
    def get_object(self, id):

        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None
        
    def get(self, request, id):
        
        author = self.get_object(id)

        if not author:
            return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        ser = AuthorSerializer(author)
        return Response(ser.data)
    

    def put(self, request, id):

        author = self.get_object(id)

        if not author:
            return Response({'error': 'author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        ser = AuthorSerializer(author, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):

        author = self.get_object(id)

        if not author:
            return Response({'error': 'author not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        ser = AuthorSerializer(author, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):

        author = self.get_object(id)
        
        if not author:
            return Response({'error': 'author not found'}, status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response({'success': f'{id} deleted'})
    


class BookListApiView(APIView):
    def get(self, request):
        book = Book.objects.all()
        ser = BookSerializer(book, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        ser = BookSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return None    
    
    def get(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
        ser = BookSerializer(book)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        book = self.get_object(id)

        if not book:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
        ser = BookSerializer(book, data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
        ser = BookSerializer(book, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def  delete(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response({'error': 'book not found'}, status=status.HTTP_400_BAD_REQUEST)
        book.delete()
        return Response({'success': f'{id} book deleted'})
    


class ArticleListApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'