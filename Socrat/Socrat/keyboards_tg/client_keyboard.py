from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_add_translate = KeyboardButton('/add_word')
button_add_book = KeyboardButton('/add_book')
button4 = KeyboardButton('/contact', request_contact=True)
button5 = KeyboardButton('/location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# one_time_keyboard = True Прятать клавиатуру после нажатия.

kb_client.add(button_add_translate)
kb_client.add(button_add_book)
kb_client.row(button4, button5)  # каждое добавление с новой строки
# insert - добавляет если есть место
# row(a, b, c) - добавление всего в одну строку
