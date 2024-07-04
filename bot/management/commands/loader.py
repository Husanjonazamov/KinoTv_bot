import logging
from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.conf import settings

API_TOKEN = settings.BOT_TOKEN or settings.TEST_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

# Boshqa sozlamalar


storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)