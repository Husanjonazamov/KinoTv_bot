import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from asyncio import create_task
from asgiref.sync import sync_to_async
from users.models import User
from bot.management.commands.users.subscription import check_subscriptions
from bot.management.commands.utils.button import get_subscription_buttons
from bot.management.commands.loader import bot, dp
from bot.management.commands.utils import texts, button

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    not_subscribed = await check_subscriptions(bot, user_id)

    # Check if the user exists in the database
    user_exists = await sync_to_async(User.objects.filter(user_id=user_id).exists)()

    # If user does not exist, create a new one
    if not user_exists:
        await sync_to_async(User.objects.create)(user_id=user_id)
        logger.info(f"New user created with user_id: {user_id}")
    else:
        logger.info(f"User with user_id: {user_id} already exists")

    if not not_subscribed:
        await message.answer(texts.START_USER, reply_markup=button.MAIN_MENU)
    else:
        keyboard = get_subscription_buttons(not_subscribed)
        await message.answer(texts.CHANNEL_REQUEST, reply_markup=keyboard)

    await state.finish()



    

@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
    await create_task(start_command(message, state))

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
