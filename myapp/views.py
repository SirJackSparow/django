from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from .prompt_serializers import PromptSerializer
from rest_framework import APIView

OLLAMA_API_URL = "http://localhost:11434/api/generate"

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


@api_view(["POST"])
def generate_text(request):
      serializer = PromptSerializer(data=request.data)
      if serializer.is_valid():
            payload = {
                  "model": serializer.validated_data["owl"],
                  "prompt": serializer.validated_data["prompt"]
            }           
            response = request.post("url", json=payload)
            return Response(response.json())
      return Response(serializer.errors, status=400)

class OllamaChatView(APIView):
      def post(self, request):
            prompt = request.data.get("prompt","")
            if not prompt:
                  return Response({"error": "Prompt is Required"}, status=400)
            try:
                  response = request.post(OLLAMA_API_URL,json={"model": "mistral", "prompt": prompt})
                  ollama_response = response.json().get("response","No Response")

                  return Response({"prompt": prompt, "response": ollama_response})
            except Exception as e:
                  return Response({"error": str(e)}, status=500)

