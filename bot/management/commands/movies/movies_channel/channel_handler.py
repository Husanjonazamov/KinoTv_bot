from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp
from bot.management.commands.movies.movies_channel.parser import parse_movie_details
from bot.management.commands.movies.movies_channel.database import save_movie_to_db
from asyncio import create_task
from aiogram import types, Dispatcher
import os


CHANNEL_ID = os.getenv('CHANNEL_ID')

async def handle_channel_post_task(message: types.Message, state: FSMContext):
    if str(message.chat.id) == CHANNEL_ID or message.chat.username == CHANNEL_ID:
        text = message.text.strip()
        title, genre, year, language, country, quality, file_id, code = parse_movie_details(text)
        await save_movie_to_db(title, genre, year, language, country, quality, file_id, code)
        await message.answer(f"Kino '{title}' kodi '{code}' bazaga saqlandi.")
    else:
        await message.answer("Bu kanal xabarlari qabul qilinmaydi.")
    print(message.video.file_id)


@dp.message_handler(content_types=['video'])
async def handle_channel_post(message: Message, state: FSMContext):
    await create_task(handle_channel_post_task(message, state))
