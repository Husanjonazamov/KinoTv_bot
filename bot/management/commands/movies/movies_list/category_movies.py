from aiogram import types
from aiogram.dispatcher import FSMContext
from asyncio import create_task
from asgiref.sync import sync_to_async
from bot.management.commands.movies.movies_list.list_func import get_movies_by_category
from bot.management.commands.utils import button, texts
from bot.management.commands.loader import dp, bot




async def show_movies_by_category_task(callback_query: types.CallbackQuery, state: FSMContext):
    category_title = callback_query.data.split('_')[1]
    movies = await sync_to_async(get_movies_by_category)(category_title)

    if movies:
        response = f"{category_title} {texts.CATEGORY_MOVIES}\n\n"
        for index, movie in enumerate(movies, start=1):
            response += f"{index}. {movie.title} ({movie.year}) - kod: {movie.code}\n\n"
        await callback_query.message.answer(response)
    else:
        await callback_query.message.answer(f"{category_title} {texts.CATEGORY_NOT_MOVIES}")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('category_'), state='*')
async def show_movies_by_category(callback_query: types.CallbackQuery, state: FSMContext):
    await create_task(show_movies_by_category_task(callback_query, state))
