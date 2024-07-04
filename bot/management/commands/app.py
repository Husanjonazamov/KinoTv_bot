import types
from typing import Any
from aiogram import executor
from .loader import dp, bot

from config.settings import ADMIN

from django.core.management.base import BaseCommand

from . import users

class Command(BaseCommand):
    help = "run bot file"


    def handle(self, *args: Any, **options: Any):
        async def on_startup(dp):
            # Adminlarga xabar yuborish
            await bot.send_message(ADMIN, "Bot ishga tushdi!")

        # disable skip_update deploy version
        executor.start_polling(dp, skip_updates=False, on_startup=on_startup)