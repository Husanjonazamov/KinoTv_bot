import os
import django
import logging
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from asyncio import create_task
from asgiref.sync import sync_to_async
from bot.management.commands.loader import dp, bot
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils import texts
from bot.management.commands.state import Movies
from bot.management.commands.utils import button
from bot.management.commands.services.services import get_episodes_by_series_code
from bot.management.commands.movies.movies_download.pyrogram_client import app







os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

async def series_task(client, message: types.Message, state: FSMContext):
    code = message.text.strip()
    user_id = message.from_user.id

    not_subscribed = await check_subscriptions(bot, user_id)

    if not_subscribed:
        keyboard = button.get_subscription_buttons(not_subscribed)
        await message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)
    else:
        # Fetch episodes by series code using the service function
        episodes_data = await sync_to_async(get_episodes_by_series_code)(code)

        if not episodes_data:
            await message.reply("Series not found or no episodes available.")
            return

        # Send each episode found
        for episode in episodes_data:
            title = episode['title']
            file_id = episode['file_id']
            caption_text = f"{title} - Episode {episode['episode_number']}"
            await bot.send_video(message.chat.id, file_id, caption=caption_text, parse_mode=types.ParseMode.HTML)

@dp.message_handler(state=Movies.code, content_types=['text'])
async def handle_message(message: Message, state: FSMContext):
    if message.text == button.BACK_TEXT:
        await state.finish()
        await message.answer(texts.MAIN_MENU, reply_markup=button.MAIN_MENU)
    else:
        await create_task(series_task(app, message, state))

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
