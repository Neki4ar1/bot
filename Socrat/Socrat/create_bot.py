"""
This module sets up a Telegram bot using the aiogram library. It initializes a Bot instance with the
Telegram API token, creates a MemoryStorage instance for storing information about the bot, and creates
a Dispatcher instance to handle incoming updates and route them to the appropriate handlers.

Functions:
    None

Classes:
    None
"""
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os

storage = MemoryStorage()

bot = Bot(token=os.getenv('TG_HOMETASK_TOKEN', 'Not_Found'))
dp = Dispatcher(bot, storage=storage)
