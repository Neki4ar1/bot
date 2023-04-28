from .models import Word, Book
from django.conf import settings
from aiogram.utils import executor
from .create_bot import dp
from .handlers import client

async def on_startup(_):
    print('starting bot')


client.register_handlers_client(dp)
# other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

#
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     await message.answer(message.text)
#     # await message.reply(message.text) # ответ на сообщение
#     # await bot.send_message(message.from_user.id, message.text) #сообщение в личку