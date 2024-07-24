from movies.models import Movie, Category, Episode
from django.shortcuts import render, get_object_or_404
from treyler.models import Treyler
from rest_framework import generics
from rest_framework.response import Response
from .serializers import MovieSerializer, Category_Serializer, TreylerSerializers, EpisodeSerializers



class MoviesList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class TreylerList(generics.ListCreateAPIView):
  queryset = Treyler.objects.all()
  serializer_class = TreylerSerializers



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer



class EpisodeList(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializers