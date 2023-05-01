"""This code is using the aiogram library to create a custom keyboard for a Telegram bot"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Define the russian names for each command
add_word_ru = '/добавить_слово'
add_book_ru = '/добавить_книгу'
send_words_ru = '/все_слова'
send_books_ru = '/все_книги'
contact_ru = '/контактные_данные'
location_ru = '/местоположение'

# Create a list of KeyboardButton objects with the russian names for each command
buttons = [
    KeyboardButton(add_word_ru),
    KeyboardButton(add_book_ru),
    KeyboardButton(send_words_ru),
    KeyboardButton(send_books_ru),
    KeyboardButton(contact_ru, request_contact=True),
    KeyboardButton(location_ru, request_location=True),
]

# Create the ReplyKeyboardMarkup object with russian buttons and options
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=2).add(*buttons)
