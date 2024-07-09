from movies.models import Movie
from asgiref.sync import sync_to_async


@sync_to_async
def update_and_get_download_count(code):
    try:
        movie = Movie.objects.get(code=code)
        movie.download_count += 1
        movie.save()
        return movie.download_count
    except Movie.DoesNotExist:
        return None
