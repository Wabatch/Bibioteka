from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework import viewsets, generics,filters
from api.serializers import BookSerializer, UsersSerializer
from book.models import Book
from users.models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class BookUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])        
def addUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def bookDetail(request, id):

    try:
        books = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(books)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data)
        return Response(serializer.erroes, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


