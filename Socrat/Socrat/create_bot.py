from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os

storage = MemoryStorage()

bot = Bot(token=os.getenv('TG_HOMETASK_TOKEN', 'Not_Found'))
dp = Dispatcher(bot, storage=storage)
