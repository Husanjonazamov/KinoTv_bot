from movies.models import Movie
from django.contrib.postgres.search import TrigramSimilarity



def search_movies_trigram(query):

    return Movie.objects.annotate(
        similarity=TrigramSimilarity('title', query) +
                   TrigramSimilarity('genre', query) +
                   TrigramSimilarity('year', query) +
                   TrigramSimilarity('language', query) +
                   TrigramSimilarity('country', query) +
                   TrigramSimilarity('quality', query)
    ).filter(similarity__gt=0.1).order_by('-similarity')
