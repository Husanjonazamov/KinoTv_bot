from celery import shared_task
from aiogram import Bot
from users.models import User
import logging
import asyncio

# Telegram bot tokeni
API_TOKEN = '6809798760:AAFoHbhh_6EqgZAG0cy603-F-RxX2ASIzi8'
bot = Bot(token=API_TOKEN)

logger = logging.getLogger(__name__)

async def send_message(user_id, message_text):
    try:
        await bot.send_message(user_id, message_text)
        logger.info(f"Message sent to user {user_id}")
    except Exception as e:
        logger.error(f"Failed to send message to {user_id}: {e}")

def notify_users_about_new_treyler(treyler_id, title, description, code):
    users = User.objects.all()
    message_text = f"Yangi treyler qo'shildi: {title}\n{description}\nKod: {code}"
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [send_message(user.user_id, message_text) for user in users]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
