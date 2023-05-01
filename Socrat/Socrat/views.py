from aiogram.utils import executor
from .create_bot import dp
from .handlers import client, add_word, add_book, other, get_all


async def on_startup(_):
    print('starting bot')


client.register_handlers_client(dp)
add_word.register_add_word(dp)
add_book.register_add_book(dp)
get_all.register_get_all(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

#
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     await message.answer(message.text)
#     # await message.reply(message.text) # ответ на сообщение
#     # await bot.send_message(message.from_user.id, message.text) #сообщение в личку
