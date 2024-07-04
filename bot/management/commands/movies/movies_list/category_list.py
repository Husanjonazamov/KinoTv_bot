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

from asgiref.sync import sync_to_async
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from bot.management.commands.movies.movies_list.list_func import get_all_categories




async def send_category_task(client, message: types.Message, state: FSMContext):
    categories = await sync_to_async(get_all_categories)()
    if categories:
        keyboard = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(text=category.title, callback_data=f"category_{category.title}") for category
                   in categories]
        for i in range(0, len(buttons), 2):
            keyboard.row(*buttons[i:i + 2])
        await message.answer(texts.CATEGORY_SELECT, reply_markup=keyboard)
    else:
        await message.answer(texts.CATEGORY_ERROR)




@dp.message_handler(
    lambda message: message.text.startswith((
                button.MOVIES_LIST,
                )), state="*", content_types=['text'])
async def movies_list(message: Message, state: FSMContext):
    await create_task(send_category_task(app, message, state))


@dp.message_handler(commands=['list'], state='*')
async def movies_list(message: Message, state: FSMContext):
    await create_task(send_category_task(app, message, state))