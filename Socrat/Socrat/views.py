"""
This code uses the aiogram library to create a Telegram bot.
It registers several handlers for different types of user messages
and starts polling for incoming updates from the Telegram API.
When the bot is started, it prints a message to the console.
The commented-out function at the bottom would respond
to any message by echoing back the same text.
"""
from aiogram.utils import executor
from .create_bot import dp
from .handlers import client, add_word, add_book, other, get_all


async def on_startup(_) -> None:
    """This function is called when the bot starts up."""
    print('starting bot')


# Register handlers for different types of messages
client.register_handlers_client(dp)
add_word.register_add_word(dp)
add_book.register_add_book(dp)
get_all.register_get_all(dp)
other.register_handlers_other(dp)

# Start polling for incoming updates from Telegram API
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# Commented-out example of a simple message handler that echoes back the same text
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     await message.answer(message.text)
#     # await message.reply(message.text) # ответ на сообщение
#     # await bot.send_message(message.from_user.id, message.text) #сообщение в личку
