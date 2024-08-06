import os
import django
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from asyncio import create_task
from pyrogram import Client
from asgiref.sync import sync_to_async
from bot.management.commands.loader import dp, bot
from bot.management.commands.movies.movies_download.movies_func import get_video_duration
from bot.management.commands.services.services import get_movie_by_code, get_episodes_by_series_code
from bot.management.commands.movies.movies_download.pyrogram_client import app, start_client, stop_client
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils import texts
from bot.management.commands.state import Movies
from bot.management.commands.movies.movies_download.download_count import update_and_get_download_count
from bot.management.commands.utils import button


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()



async def movies_task(client, message: types.Message, state: FSMContext):
    code = message.text.strip()
    movie_data = get_movie_by_code(code)
    user_id = message.from_user.id

    not_subscribed = await check_subscriptions(bot, user_id)

    if not_subscribed:
        keyboard = button.get_subscription_buttons(not_subscribed)
        await message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)
    else:
        if movie_data:
            movie_file_url = movie_data.get('file_id')

            if not movie_file_url:
                await message.reply("Movie file URL is invalid.")
                return

            title = movie_data.get('title')
            year = movie_data.get('year')
            language = movie_data.get('language')
            quality = movie_data.get('quality')
            country = movie_data.get('country')
            genre = movie_data.get('genre')

            download_count = await update_and_get_download_count(code)

            if download_count is None:
                await message.reply("Movie not found in the database.")
                return

            caption_text = texts.MOVIES_SEND(
                title=title,
                year=year,
                language=language,
                quality=quality,
                country=country,
                genre=genre,
                download_count=download_count
            )

            await message.answer_video(
                video=movie_file_url,
                caption=caption_text,
                reply_markup=button.create_movie_buttons()
            )

            episodes_data = await sync_to_async(get_episodes_by_series_code)(code)
            # if not episodes_data:
            #     await message.reply("Series not found or no episodes available.")
            #     return

            for episode in episodes_data:
                episode_title = episode['title']
                episode_year = episode['year']
                episode_language = episode['language']
                episode_quality = episode['quality']
                episode_country = episode['country']
                episode_genre = episode['genre']
                episode_file_id = episode['file_id']
                episode_number = episode['episode_number']
                episode_download_count = await update_and_get_download_count(code)

                if download_count is None:
                    await message.reply("Movie not found in the database.")
                    return

                episode = texts.EPISODE(
                    episode_title=episode_title,
                    episode_year=episode_year,
                    episode_language=episode_language,
                    episode_quality=episode_quality,
                    episode_country=episode_country,
                    episode_genre=episode_genre,
                    episode_number=episode_number,
                    episode_download_count=episode_download_count
                )

                await message.answer_video(
                    video=episode_file_id,
                    caption=episode,
                    reply_markup=button.create_movie_buttons()
                )

        else:
            await message.answer(texts.KOD_IS_NOT)

@dp.message_handler(state=Movies.code, content_types=['text'])
async def handle_message(message: Message, state: FSMContext):
    if message.text == button.BACK_TEXT:
        await state.finish()
        await message.answer(texts.MAIN_MENU, reply_markup=button.MAIN_MENU)
    else:
        await create_task(movies_task(app, message, state))

