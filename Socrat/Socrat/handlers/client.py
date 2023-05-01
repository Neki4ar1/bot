"""
This code is defining a handler function command_start that gets registered
with the Dispatcher object dp to handle /start and /help commands.
When either of these commands are issued, this handler sends a message
to the user containing a description of the bot
along with a custom keyboard provided by kb_client
"""
from aiogram import types, Dispatcher
from ..create_bot import bot
from ..keyboards_tg.client_keyboard import kb_client


async def command_start(message: types.Message) -> None:
    """
    Responds to the /start and /help commands by sending a message with a description of the bot.

    :param message: The Message object containing the command.
    """
    txt = "<i>Здравствуйте, я бот <b>Сократ</b>, названный в честь великого философа, который " \
          "известен своим методом диалога и помогает людям мыслить логически и критически. " \
          "Моя задача - помогать вам изучать иностранные языки.</i>"
    await bot.send_message(message.from_user.id, txt, reply_markup=kb_client, parse_mode='HTML')


def register_handlers_client(dp: Dispatcher) -> None:
    """
    Registers the command_start function as the handler for the /start and /help commands.

    :param dp: The Dispatcher object used to register the handler.
    """
    dp.register_message_handler(command_start, commands=['start', 'help'])
