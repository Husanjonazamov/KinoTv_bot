from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp
from asyncio import create_task

from bot.management.commands.state import Movies
from bot.management.commands.utils import texts
from bot.management.commands.utils import button



async def movies_handler_task(message: Message, state: FSMContext):

    await message.answer(texts.DOWNLOAD_MOVIES_HANDLER, reply_markup=button.BACK)

    await state.set_state(Movies.code)


@dp.message_handler(
    lambda message: message.text.startswith((
                button.DOWNLOAD_MOVIES,
                )), state="*", content_types=['text'])
async def movies_handler(message: Message, state: FSMContext):
    create_task(movies_handler_task(message, state))

