from aiogram.dispatcher import FSMContext
from bot.management.commands.loader import dp, bot
from aiogram import types
from asyncio import create_task




async def inline_query_handler_task(inline_query: types.InlineQuery):
    try:
        # Inline query natijalarini yaratish
        results = [
            types.InlineQueryResultArticle(
                id="1",
                title="Do'stlarga ulashish",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{inline_query.query}"
                ),
                description="Kino ulashish",
                thumb_url="https://example.com/thumb.jpg"  # Kino posteri URL ni kiriting
            )
        ]
        await inline_query.answer(results)
    except Exception as e:
        await inline_query.answer(f"Xabarni ulashishda xatolik yuz berdi: {e}")


@dp.inline_handler()
async def inline_query_handler(inline_query: types.InlineQuery, state: FSMContext):
  create_task(inline_query_handler_task(inline_query, state))