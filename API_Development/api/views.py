from django.shortcuts import render
from rest_framework import generics
from .Serializers import BlogPostSerializer
from .models import Blogpost    
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=BlogPostSerializer

class BlogPostRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=BlogPostSerializer
    lookup_field="pk"
