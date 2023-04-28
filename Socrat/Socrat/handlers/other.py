from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer("Не знаю, что на это ответить.")
    # await message.reply(message.text) # ответ на сообщение
#     # await bot.send_message(message.from_user.id, message.text) #сообщение в личку


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
