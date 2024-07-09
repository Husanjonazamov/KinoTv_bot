import logging
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import bot
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils import texts, button
from bot.management.commands.utils.button import get_subscription_buttons
from bot.management.commands.loader import bot, dp
from aiogram.dispatcher import FSMContext
from asyncio import create_task



async def check_subscriptions_callback(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    not_subscribed = await check_subscriptions(bot, user_id)

    if not not_subscribed:
        await call.message.delete()
        await call.message.answer(texts.CHANNEL_CHECK, reply_markup=button.MAIN_MENU)
        # Call your main menu function here
    else:
        await call.message.delete()
        keyboard = get_subscription_buttons(not_subscribed)
        await call.message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)




@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("check_subscriptions"), state="*")
async def check(call: types.CallbackQuery, state: FSMContext):
  await create_task(check_subscriptions_callback(call, state))