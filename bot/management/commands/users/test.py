import logging
from bot.management.commands.loader import dp, bot
from aiogram import Bot, Dispatcher, executor, types




@dp.message_handler(content_types=['video'])
async def echo(message: types.Message):
    videos = message.video.file_id
    print(videos)
    await message.answer(videos)

