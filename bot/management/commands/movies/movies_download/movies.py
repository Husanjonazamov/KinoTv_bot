from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from asyncio import create_task
from pyrogram import Client
from bot.management.commands.loader import dp, bot
from bot.management.commands.movies.movies_download.movies_func import get_video_duration
from bot.management.commands.services.services import get_movie_by_code
from bot.management.commands.movies.movies_download.pyrogram_client import app, start_client, stop_client  # Import client and functions from pyrogram_client.py
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils import texts

from bot.management.commands.state import Movies
from bot.management.commands.utils import button




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

            # Check if movie_file_url is valid
            if not movie_file_url:
                await message.reply("Movie file URL is invalid.")
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

            await message.answer_video(
                    video=movie_file_url,
                    caption=caption_text,
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
