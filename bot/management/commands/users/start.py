import logging
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import bot
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils.button import get_subscription_buttons
from bot.management.commands.loader import bot, dp
from aiogram.dispatcher import FSMContext
from asyncio import create_task
from bot.management.commands.utils import texts, button



async def start_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    not_subscribed = await check_subscriptions(bot, user_id)


    if not not_subscribed:
        await message.answer(texts.START_USER, reply_markup=button.MAIN_MENU)
        # Call your main menu function here
    else:
        keyboard = get_subscription_buttons(not_subscribed)
        await message.answer(texts.CHANNEL_REQUEST, reply_markup=keyboard)
    await state.finish()


@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
  await create_task(start_command(message, state))
