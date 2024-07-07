from movies.models import Movie
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q

def search_movies_trigram(query):
    return Movie.objects.annotate(
        similarity_title=TrigramSimilarity('title', query),
        similarity_genre=TrigramSimilarity('genre', query),
        similarity_language=TrigramSimilarity('language', query),
        similarity_country=TrigramSimilarity('country', query),
        similarity_quality=TrigramSimilarity('quality', query),
        similarity_code=TrigramSimilarity('code', query),
    ).filter(
        Q(similarity_title__gt=0.1) | Q(similarity_genre__gt=0.1) |
        Q(similarity_language__gt=0.1) | Q(similarity_country__gt=0.1) |
        Q(similarity_quality__gt=0.1) | Q(similarity_code__gt=0.1)
    ).order_by(
        '-similarity_title', '-similarity_genre', '-similarity_language',
        '-similarity_country', '-similarity_quality', '-similarity_code'
    )
