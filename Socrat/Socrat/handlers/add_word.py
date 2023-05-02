"""
This code defines a Telegram bot functionality
to add new words and their translations to a database
using a finite state machine.
It also uses an asynchronous library aiogram
for handling messages and states.
"""
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from ..models import Word
from asgiref.sync import sync_to_async

TO_CANCEL = 'добавить_книгу добавить_слово все_слова все_книги /контактные_данные /местоположение'


@sync_to_async
def create_word(word, translate, user_id) -> None:
    """Создать новый объект класса Word с заданным словом и его переводом"""
    Word.objects.create(word=word, translate=translate, user_id=user_id)


class FSMword(StatesGroup):
    """Определяет состояния для машины состояний, используемой для добавления нового слова"""
    word = State()
    translate = State()
    user_id = State()


async def add_start(message: types.Message) -> None:
    """Функция для начала процесса добавления нового слова"""
    await FSMword.word.set()
    await message.reply('Введите новое слово. \nДля отмены напишите <b>"отмена"</b>.', parse_mode='HTML')


async def cancel_add(message: types.Message, state: FSMword) -> None:
    """Функция для отмены процесса добавления нового слова"""
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Добавление отменено')


async def add_word(message: types.Message, state: FSMword) -> None:
    """Функция для добавления нового слова в базу данных"""
    if message.text in TO_CANCEL:
        await message.reply('Ошибка. Вы отправили новую команду.')
        await cancel_add(message, state)
        return

    async with state.proxy() as data:
        data['word'] = message.text
        data['user_id'] = message.from_user.id
    await FSMword.next()
    await message.reply('Введите перевод этого слова. \nДля отмены напишите <b>"отмена"</b>.', parse_mode='HTML')


async def add_translation(message: types.Message, state: FSMContext) -> None:
    """Функция для добавления перевода слова в базу данных"""
    async with state.proxy() as data:
        data['translate'] = message.text

    async with state.proxy() as data:
        await create_word(data['word'], data['translate'], data['user_id'])
        await message.answer(text='Перевод добавлен!')
    await state.finish()


def register_add_word(dp: Dispatcher) -> None:
    """Функция для регистрации обработчиков для добавления нового слова"""
    # dp.register_message_handler(add_start, commands=['add_word'], state=None)
    dp.register_message_handler(add_start, state='*', commands='добавить_слово')
    dp.register_message_handler(add_start, Text(equals='добавить_слово', ignore_case=True), state="*")
    dp.register_message_handler(cancel_add, state='*', commands='отмена')
    dp.register_message_handler(cancel_add, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(add_word, state=FSMword.word)
    dp.register_message_handler(add_translation, state=FSMword.translate)
