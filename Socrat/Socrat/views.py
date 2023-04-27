from .models import Word, Book
from django.conf import settings

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


import os


bot = Bot(token=settings.TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo_send(message: types.Message):
    txt = 'Это авторский бот Сократ, который помогает при изучении иностранных языков.'
    await message.reply(message.text)

executor.start_polling(dp, skip_updates=True)
