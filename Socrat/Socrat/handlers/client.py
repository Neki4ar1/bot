from aiogram import types, Dispatcher
from ..create_bot import bot
from ..keyboards_tg.client_keyboard import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    txt = 'Это авторский бот Сократ, который помогает при изучении иностранных языков.'
    await bot.send_message(message.from_user.id, txt, reply_markup=kb_client)


# @dp.message_handler(commands=['test1'])
# async def test1(message: types.Message):
#     await message.answer('test')


# @dp.message_handler(commands=['test2'])
# async def test2(message: types.Message):
#     await message.answer('more tests')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    # dp.register_message_handler(add_word(), commands=['add_word'])
    # dp.register_message_handler(test2, commands=['test2'])
