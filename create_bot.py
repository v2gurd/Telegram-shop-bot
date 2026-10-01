from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# Telegram Bot
TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = 7763255760

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
