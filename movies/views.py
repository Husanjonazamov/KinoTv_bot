
from .models import Movie, Category
# movies/views.py
from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from .models import Movie
from api.serializers import MovieSerializer, Category_Serializer
from django.http import JsonResponse




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



def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movies_detail.html', {'movie': movie})





def get_episodes_by_series_code(request, code):
    try:
        series = Movie.objects.get(code=code)
        episodes = series.episodes.all()
        episodes_data = [
            {
                'title': episode.title,
                'year': series.year,
                'language': series.language,
                'quality': series.quality,
                'country': series.country,
                'genre': series.genre,
                'file_id': episode.file_id,
                'episode_number': episode.episode_number,
                'download_count': episode.download_count
            } for episode in episodes
        ]
        return JsonResponse({'episodes': episodes_data})
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Series not found'}, status=404)
