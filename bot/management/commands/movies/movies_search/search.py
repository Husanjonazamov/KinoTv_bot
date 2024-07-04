from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot.management.commands.loader import dp
from bot.management.commands.state import MoviesSearch
from bot.management.commands.utils import button, texts
from asyncio import create_task
from bot.management.commands.movies.movies_search.search_servis import search_movies_trigram
from asgiref.sync import sync_to_async
import logging


async def search_movies_task(message: Message, state: FSMContext):
    query = message.text.strip()
    logging.info(f"Searching for movies with query: {query}")
    movies = await sync_to_async(search_movies_trigram)(query)

    if movies:
        response = "Natijalar:\n"
        keyboard = InlineKeyboardMarkup(row_width=1)
        for index, movie in enumerate(movies, start=1):
            button_text = f"🎬 {movie.title}"
            button_callback_data = f"{movie.code}"  # Faqat kino kodi
            keyboard.add(InlineKeyboardButton(text=button_text, callback_data=button_callback_data))
            response += f"{index}. {movie.title} - Kodi: {movie.code}\n\n"

        await message.answer(response, reply_markup=keyboard)
        logging.info("Search results displayed.")
    else:
        await message.answer(texts.SEARCH_NOT_FOUND)
        await state.set_state(MoviesSearch.waiting_for_query)


@dp.message_handler(state=MoviesSearch.waiting_for_query, content_types=['text'])
async def search_movies(message: Message, state: FSMContext):
    text = message.text
    logging.info(f"Received search query: {text}")
    if text == button.BACK_TEXT:
        await state.finish()
        await message.answer(texts.MAIN_MENU, reply_markup=button.MAIN_MENU)
        logging.info("Back button pressed, returning to main menu.")
    else:
        await create_task(search_movies_task(message, state))
