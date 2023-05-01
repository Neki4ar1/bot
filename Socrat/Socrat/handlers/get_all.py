"""
This code defines two functions,
send_words and send_books,
and registers them as message handlers
with the aiogram library's Dispatcher.
"""
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from ..models import Word, Book
from ..create_bot import bot
from asgiref.sync import sync_to_async


@sync_to_async
def get_words() -> list[list[int, str, str]]:
    """
    Retrieve all Word objects from the database and return them as a list of lists.
    Each inner list contains the index of the word (starting from 1), the word itself,
    and its translation.

    Returns:
        List of lists containing Word objects.
    """
    words = []
    for i, item in enumerate(Word.objects.all()):
        words.append([i+1, item.word, item.translate])
    return words


@sync_to_async
def get_books() -> list[list[int, str, str]]:
    """
    Retrieve all Book objects from the database and return them as a list of lists.
    Each inner list contains the index of the book (starting from 1), the name of the book,
    and its URL.

    Returns:
        List of lists containing Book objects.
    """
    books = []
    for i, item in enumerate(Book.objects.all()):
        books.append([i+1, item.name, item.url])
    return books


async def send_words(message: types.Message) -> None:
    """
    Send all Word objects to the user who triggered this function as a message.
    Each word is sent as a separate message with formatting such that the word is
    followed by its translation in italics.

    Args:
        message: The message object that triggered this function.
    """
    for item in await get_words():
        await bot.send_message(message.from_user.id, f'{item[1]} - _{item[2]}_', parse_mode='Markdown')


async def send_books(message: types.Message) -> None:
    """
    Send all Book objects to the user who triggered this function as a message.
    Each book is sent as a separate message with formatting such that the name of
    the book is followed by its URL.

    Args:
        message: The message object that triggered this function.
    """
    for item in await get_books():
        await bot.send_message(message.from_user.id, f'{item[1]} - {item[2]}', parse_mode='Markdown')


def register_get_all(dp: Dispatcher) -> None:
    """
    Register the send_words and send_books handlers with the provided Dispatcher.

    Args:
        dp: The Dispatcher to which the handlers will be added.
    """
    dp.register_message_handler(send_words, commands=['все_слова'], state=None)
    dp.register_message_handler(send_words, Text(equals='все_слова', ignore_case=True), state="*")
    dp.register_message_handler(send_books, commands=['все_книги'], state=None)
    dp.register_message_handler(send_books, Text(equals='все_книги', ignore_case=True), state="*")
