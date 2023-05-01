from aiogram.dispatcher import Dispatcher
from aiogram import types
from ..models import Word, Book
from ..create_bot import bot
from asgiref.sync import sync_to_async


@sync_to_async
def get_words():
    words = []
    for i, item in enumerate(Word.objects.all()):
        words.append([i+1, item.word, item.translate])
    return words


@sync_to_async
def get_books():
    books = []
    for i, item in enumerate(Book.objects.all()):
        books.append([i+1, item.name, item.url])
    return books


async def send_words(message: types.Message):
    for item in await get_words():
        await bot.send_message(message.from_user.id, f'{item[1]} - _{item[2]}_', parse_mode='Markdown')


async def send_books(message: types.Message):
    for item in await get_books():
        await bot.send_message(message.from_user.id, f'{item[1]} - {item[2]}', parse_mode='Markdown')


def register_get_all(dp: Dispatcher):
    dp.register_message_handler(send_words, commands=['send_words'], state=None)
    dp.register_message_handler(send_books, commands=['send_books'], state=None)
