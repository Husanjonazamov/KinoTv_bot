import logging
import asyncio
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Treyler
from users.models import User
from aiogram import Bot

# Telegram bot token
API_TOKEN = '6809798760:AAFoHbhh_6EqgZAG0cy603-F-RxX2ASIzi8'
bot = Bot(token=API_TOKEN)


logger = logging.getLogger(__name__)

@receiver(post_save, sender=Treyler)
def send_new_treyler_notification(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New Treyler created: {instance.title}")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(notify_users())



async def notify_users():
    logger.info("Starting to notify users.")
    users = User.objects.all()
    message_text = "salom"

    for user in users:
        try:
            await bot.send_message(user.user_id, message_text)
            logger.info(f"Message sent to user {user.user_id}")
        except Exception as e:
            logger.error(f"Failed to send message to {user.user_id}: {e}")
    logger.info("Finished notifying users.")
