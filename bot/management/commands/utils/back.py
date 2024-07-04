from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp
from bot.management.commands.utils import button, texts
from asyncio import create_task


async def back(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(texts.MAIN_MENU, reply_markup=button.MAIN_MENU)


@dp.message_handler(
    lambda message: message.text.startswith((
                button.BACK_TEXT,
                )), state="*", content_types=['text'])
async def search(message: Message, state: FSMContext):
  create_task(back(message, state))