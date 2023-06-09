"""
The code is a Python script that defines functions and a state machine using the aiogram library,
which is an asynchronous framework for building Telegram bots.
The functions are used to handle user input and update the bot's state accordingly.
"""
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from ..models import Book
from asgiref.sync import sync_to_async
TO_CANCEL = 'добавить_книгу добавить_слово все_слова все_книги /контактные_данные /местоположение'


@sync_to_async
def create_book(name, url, user_id) -> None:
    """Создать новый объект класса Book с заданным именем и URL"""
    Book.objects.create(name=name, url=url, user_id=user_id)


class FSMbook(StatesGroup):
    """Определяет состояния для машины состояний, используемой для добавления новой книги"""
    name = State()
    url = State()
    user_id = State()


async def book_add_start(message: types.Message) -> None:
    """Функция для начала процесса добавления новой книги"""
    await FSMbook.name.set()
    await message.reply('Введите название книги. \nДля отмены напишите <b>"отмена"</b>.', parse_mode='HTML')


async def cancel_add_book(message: types.Message, state: FSMbook) -> None:
    """Функция для отмены процесса добавления новой книги"""
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Добавление отменено')


async def add_book_name(message: types.Message, state: FSMbook) -> None:
    """Функция для добавления имени новой книги"""
    if message.text in TO_CANCEL:
        await message.reply('Ошибка. Вы отправили новую команду.')
        await cancel_add_book(message, state)
        return
    async with state.proxy() as data:
        data['name'] = message.text
        data['user_id'] = message.from_user.id

    await FSMbook.next()
    await message.reply('Введите URL книги. \nДля отмены напишите "отмена".', parse_mode='HTML')


async def add_book_url(message: types.Message, state: FSMbook) -> None:
    """Функция для добавления URL новой книги"""
    async with state.proxy() as data:
        data['url'] = message.text

    async with state.proxy() as data:
        await create_book(data['name'], data['url'], data['user_id'])
        await message.answer(text='Книга добавлена!')
    await state.finish()


def register_add_book(dp: Dispatcher) -> None:
    """Функция для регистрации обработчиков для добавления новой книги"""
    # dp.register_message_handler(book_add_start, commands=['add_book'], state=None)
    dp.register_message_handler(book_add_start, state='*', commands='добавить_книгу')
    dp.register_message_handler(book_add_start, Text(equals='добавить_книгу', ignore_case=True), state="*")
    dp.register_message_handler(cancel_add_book, state='*', commands='отмена')
    dp.register_message_handler(cancel_add_book, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(add_book_name, state=FSMbook.name)
    dp.register_message_handler(add_book_url, state=FSMbook.url)
