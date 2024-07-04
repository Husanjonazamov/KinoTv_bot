from aiogram import types
from bot.management.commands.loader import dp
from bot.management.commands.movies.movies_search.search_servis import search_movies_trigram
from asgiref.sync import sync_to_async




@dp.inline_handler()
async def inline_query_handler(inline_query: types.InlineQuery):
    query = inline_query.query or " "
    movies = await sync_to_async(search_movies_trigram)(query)

    results = []
    if movies:
        for movie in movies:
            results.append(
                types.InlineQueryResultArticle(
                    id=str(movie.id),
                    title=movie.title,
                    input_message_content=types.InputTextMessageContent(
                        message_text=f"🎬 {movie.title}\nKod: {movie.code}\nJanr: {movie.genre}\nYil: {movie.year}\nTil: {movie.language}\nDavlat: {movie.country}\nSifat: {movie.quality}"
                    ),
                    description=f"{movie.title} - {movie.genre} - {movie.year}",
                    thumb_url="your_movie_thumbnail_url"  # Agar sizda thumbnail URL bo'lsa, uni qo'shing
                )
            )
    await inline_query.answer(results, cache_time=1)