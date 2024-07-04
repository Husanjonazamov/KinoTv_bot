from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.management.commands.loader import dp, bot
from bot.management.commands.movies.movies_download.movies import movies_task
from bot.management.commands.services.services import get_movie_by_code
from bot.management.commands.state import MoviesSearch
import logging
from asyncio import create_task
from asgiref.sync import sync_to_async
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils import button, texts
from movies.models import Movie



async def download_movie_by_code(code):
    try:
        movie = await sync_to_async(Movie.objects.get)(code=code)
        return movie
    except Movie.DoesNotExist:
        return None



async def download_movie_task(callback_query: types.CallbackQuery, state: FSMContext):
    code = callback_query.data
    logging.info(f"Downloading movie with code: {code}")

    # Bazadan kinoni yuklab olish uchun kerakli funksiya
    movie_data = await sync_to_async(get_movie_by_code)(code)
    user_id = callback_query.message.from_user.id

    not_subscribed = await check_subscriptions(bot, user_id)

    if not_subscribed:
        keyboard = button.get_subscription_buttons(not_subscribed)
        await callback_query.message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)
    else:
        if movie_data:
            movie_file_url = movie_data.get('file_id')

            # Check if movie_file_url is valid
            if not movie_file_url:
                await callback_query.message.reply("Movie file URL is invalid.")
                return

            title = movie_data.get('title')
            year = movie_data.get('year')
            language = movie_data.get('language')
            quality = movie_data.get('quality')
            country = movie_data.get('country')
            genre = movie_data.get('genre')

            caption_text = texts.MOVIES_SEND(
                title=title,
                year=year,
                language=language,
                quality=quality,
                country=country,
                genre=genre
            )

            await callback_query.message.answer_video(
                video=movie_file_url,
                caption=caption_text,
                reply_markup=button.create_movie_buttons()
            )
        else:
            await callback_query.message.answer(texts.KOD_IS_NOT)
    await state.set_state(MoviesSearch.waiting_for_query)


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.isdigit(), state="*")
async def download_movie(callback_query: types.CallbackQuery, state: FSMContext):
    await create_task(download_movie_task(callback_query, state))