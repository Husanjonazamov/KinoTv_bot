from movies.models import Movie
from asgiref.sync import sync_to_async
import logging

async def save_movie_to_db(title, genre, year, language, country, quality, file_id, code):
    try:
        movie = Movie(
            title=title,
            genre=genre,
            year=year,
            language=language,
            country=country,
            quality=quality,
            file_id=file_id,
            code=code
        )
        await sync_to_async(movie.save)()
    except Exception as e:
        logging.error(f"Error saving movie: {e}")

async def search_in_db(query):
    return await sync_to_async(Movie.objects.filter)(title__icontains=query)

async def download_movie_by_code(code):
    try:
        movie = await sync_to_async(Movie.objects.get)(code=code)
        return movie
    except Movie.DoesNotExist:
        return None
