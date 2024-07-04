import os
import requests
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from asyncio import create_task
from bot.management.commands.loader import dp, bot
from bot.management.commands.services.services import get_movie_by_list
from bot.management.commands.movies.movies_download.pyrogram_client import app
from bot.management.commands.utils import texts, button  # Import upload function

async def movies_list_task(client, message: types.Message, state: FSMContext):
    movies = get_movie_by_list()

    if movies:
        response_text = ""
        for movie in movies:
            title = movie.get('title')
            code = movie.get('code')

            response_text += texts.MOVIES_LIST_SEND(
                title=title,
                code=code
            )
        await message.answer(
            text=response_text
        )
    else:
        await message.answer(texts.KOD_IS_NOT)

@dp.message_handler(commands=['list'], state='*')
async def movies_list(message: Message, state: FSMContext):
    create_task(movies_list_task(app, message, state))



@dp.message_handler(
    lambda message: message.text.startswith((
                button.MOVIES_LIST,
                )), state="*", content_types=['text'])
async def movies_list(message: Message, state: FSMContext):
    create_task(movies_list_task(app, message, state))
