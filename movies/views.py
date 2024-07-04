
from .models import Movie, Category
# movies/views.py
from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer, Category_Serializer


class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'code'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        movie = get_object_or_404(Movie, code=code)
        data = {
            "title": movie.title,
            "genre": movie.genre,
            "year": movie.year,
            "quality": movie.quality,
            "language": movie.language,
            "country": movie.country,
        }
        if movie.file_id:
            data["file_id"] = movie.file_id
        else:
            data["movie_file"] = request.build_absolute_uri(movie.movie_file.url)
        return Response(data)




class MoviesList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movies_detail.html', {'movie': movie})


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
