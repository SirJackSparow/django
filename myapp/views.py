from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.response import Response 

# Create your views here.

#Create List
class BookListCreateView(generics.ListCreateAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer

      def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serialize = self.get_serializer(queryset,many=True)
            return Response({"data": serialize.data})


#Create Retrive, Update, Delete Book
class BookRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer      
