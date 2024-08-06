import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from asyncio import create_task
from bot.management.commands.loader import dp
from bot.management.commands.movies.movies_download.pyrogram_client import app
from bot.management.commands.utils import texts  # Import upload function

from asgiref.sync import sync_to_async
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot.management.commands.movies.treyler.treyler_list import get_treyler_all

from bot.management.commands.state import Treyler

ADMIN_ID = 6415392394

# Treylersni saqlash uchun global o'zgaruvchi
treyler_dict = {}


async def send_treyler_task(client, message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        treyler = await sync_to_async(get_treyler_all)()
        if treyler:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = [KeyboardButton(text=category.title) for category in treyler]
            for i in range(0, len(buttons), 2):
                keyboard.row(*buttons[i:i + 2])
            await message.answer(texts.TREYLER_SUCCES, reply_markup=keyboard)
            # Treylerlarni lug'atga saqlash
            treyler_dict[message.chat.id] = {treylers.title: treylers.treyler_id for treylers in treyler}
        else:
            await message.answer(texts.TREYLER_SUCCES)
    else:
        await message.answer(texts.NOT_ADMIN)
        return


    await state.set_state(Treyler.treyler_title)


@dp.message_handler(commands=['admin'], state='*')
async def movies_list(message: Message, state: FSMContext):
    await create_task(send_treyler_task(app, message, state))



