from aiogram import types
from bot.management.commands.loader import dp, bot
from aiogram.dispatcher import FSMContext
from asyncio import create_task




async def callback_delete_task(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except Exception as e:
        await call.answer(f"Xabarni o'chirishda xatolik yuz berdi")



@dp.callback_query_handler(lambda call: call.data == 'delete', state="*")
async def callback_delete(call: types.CallbackQuery, state: FSMContext):
  create_task(callback_delete_task(call, state))
