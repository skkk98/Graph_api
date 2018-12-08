from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
# Create your views here.
def hi(request):
    return HttpResponse('hi')

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer    
