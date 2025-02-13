from telegram import Bot

from app.pkg.settings import settings

bot = Bot(settings.TELEGRAM_TOKEN)

async def send_telegram_message(message: str):
    await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)
