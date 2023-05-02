from aiogram import types, Dispatcher
from ..create_bot import bot
import random
from .Quotes import socrates_quotes, size


# @dp.message_handler()
async def echo_send(message: types.Message):
    number = random.randint(1, size)
    await message.reply("Я бот, всего лишь имитация собеседника. "
                        "Я не понимаю, что вы пишете вне рамок моих команд. "
                        "Возможно вам поможет мудрость от Сократа")
    await bot.send_message(message.from_user.id, f'<i>\"{socrates_quotes[number]}</i>\" \u00A9', parse_mode='HTML')
    # await message.reply(message.text) # ответ на сообщение
    # await bot.send_message(message.from_user.id, message.text) #сообщение в личку


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
