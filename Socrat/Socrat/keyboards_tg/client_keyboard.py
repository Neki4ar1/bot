from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_add_translate = KeyboardButton('/add_word')
button_add_book = KeyboardButton('/add_book')
button_get_words = KeyboardButton('/send_words')
button_get_books = KeyboardButton('/send_books')
button4 = KeyboardButton('/contact', request_contact=True)
button5 = KeyboardButton('/location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# one_time_keyboard = True Прятать клавиатуру после нажатия.

kb_client.row(button_add_translate, button_get_words)
kb_client.row(button_add_book, button_get_books)
kb_client.row(button4, button5)  # каждое добавление с новой строки
# insert - добавляет если есть место
# row(a, b, c) - добавление всего в одну строку
