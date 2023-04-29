from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from ..models import Book
from asgiref.sync import sync_to_async


@sync_to_async
def create_book(name, url):
    Book.objects.create(name=name, url=url)


class FSMbook(StatesGroup):
    name = State()
    url = State()


async def book_add_start(message: types.Message):
    await FSMbook.name.set()
    await message.reply('Write name of the book')


async def cancel_add_book(message: types.Message, state: FSMbook):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Adding was canceled')


async def add_book_name(message: types.Message, state: FSMbook):
    async with state.proxy() as data:
        data['name'] = message.text

    await FSMbook.next()
    await message.reply('Write url of the book')


async def add_book_url(message: types.Message, state: FSMbook):
    async with state.proxy() as data:
        data['url'] = message.text

    async with state.proxy() as data:
        await create_book(data['name'], data['url'])
        await message.answer(text='Book added!')
    await state.finish()


def register_add_book(dp: Dispatcher):
    dp.register_message_handler(book_add_start, commands=['add_book'], state=None)
    dp.register_message_handler(cancel_add_book, state='*', commands='cancel')
    dp.register_message_handler(cancel_add_book, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(add_book_name, state=FSMbook.name)
    dp.register_message_handler(add_book_url, state=FSMbook.url)
