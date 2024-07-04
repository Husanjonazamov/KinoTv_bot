from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp
from bot.management.commands.state import MoviesSearch
from bot.management.commands.utils import button, texts
from asyncio import create_task



async def search_start(message: Message, state: FSMContext):

    await message.answer(texts.MOVIES_SEARCH, reply_markup=button.BACK)

    await MoviesSearch.waiting_for_query.set()


@dp.message_handler(
    lambda message: message.text.startswith((
                button.SEARCH,
                )), state="*", content_types=['text'])
async def search(message: Message, state: FSMContext):
  create_task(search_start(message, state))