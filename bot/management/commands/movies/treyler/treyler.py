from aiogram.dispatcher import FSMContext
from asyncio import create_task
from aiogram import types
from bot.management.commands.state import Treyler
from bot.management.commands.services.services import treyler_list
from bot.management.commands.utils import texts, button
from bot.management.commands.loader import dp


async def treyler_task(message: types.Message, state: FSMContext):
    text = message.text.strip()
    print(text)
    treyler_data = treyler_list(text)

    if treyler_data:
        treyler_file_url = treyler_data.get('treyler_id')
        title = treyler_data.get('title')
        description = treyler_data.get('description')
        code = treyler_data.get('code')

        coption_text = texts.TREYLER_SEND(
            title=title,
            description=description,
            code=code
        )

        await message.answer_video(
            video=treyler_file_url,
            caption=coption_text,
            reply_markup=button.treyler_send(title)
        )

    await state.finish()
@dp.message_handler(content_types=["text"], state=Treyler.treyler_title)
async def treyler_title(message: types.Message, state: FSMContext):
    await create_task(treyler_task(message, state))

