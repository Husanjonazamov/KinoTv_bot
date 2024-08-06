import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode, CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.management.commands.loader import dp, bot
from users.models import User
from treyler.models import Treyler
from bot.management.commands.utils import texts

ADMIN_ID = 6415392394

async def notify_users_with_trailer(title):
    users = User.objects.all()

    try:
        treyler = Treyler.objects.get(title=title)
        message_text = texts.TREYLER_SEND(
            title=treyler.title,
            description=treyler.description,
            code=treyler.code
        )

    except Treyler.DoesNotExist:
        return

    for user in users:
        try:
            await bot.send_video(user.user_id, treyler.treyler_id, caption=message_text, parse_mode=ParseMode.HTML)
        except Exception as e:
            print(f'Error sending video to user {user.user_id}: {e}')

async def send_message_to_all_task(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.from_user.id == ADMIN_ID:
        try:
            data = callback_query.data.split(':')
            if len(data) == 2 and data[0] == 'treyler':
                title = data[1]
                await callback_query.message.reply(f"{title} nomli treyler barcha foydalanuvchilarga yubormoqda...")
                await notify_users_with_trailer(title)
            else:
                await callback_query.answer("Invalid callback data format.")
        except ValueError:
            await callback_query.answer("Invalid trailer title.")
    else:
        await callback_query.answer(texts.NOT_ADMIN)
        return

@dp.callback_query_handler(lambda c: c.data.startswith('treyler:'), state='*')
async def handle_treyler_callback(callback_query: CallbackQuery, state: FSMContext):
    # Debug print to check callback data
    print(f"Callback Data: {callback_query.data}")
    await send_message_to_all_task(callback_query, state)

