import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Command
from users.models import User
import asyncio
from bot.management.commands.loader import dp, bot
from treyler.models import Treyler
from bot.management.commands.utils import texts
from asyncio import create_task
from aiogram.dispatcher import FSMContext




ADMIN_ID = 6415392394




async def send_message_to_all_task(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        await message.reply("Sending the latest trailer to all users...")
        await notify_users()
    else:
        await message.answer(texts.NOT_ADMIN)
        return



async def notify_users():
    users = User.objects.all()


    try:
        latest_trailer = Treyler.objects.latest('id')  # Get the latest trailer
        title = latest_trailer.title
        description = latest_trailer.description
        code = latest_trailer.code

        message_text = texts.TREYLER_SEND(
            title=title,
            description=description,
            code=code
        )

    except Treyler.DoesNotExist:
        return

    for user in users:
        try:
            await bot.send_video(user.user_id, latest_trailer.treyler_id, caption=message_text, parse_mode=ParseMode.HTML)
        except Exception as e:
            print('--')


@dp.message_handler(commands=['admin'], state="*")
async def send_message_to_all(message: types.Message, state: FSMContext):
    await create_task(send_message_to_all_task(message, state))