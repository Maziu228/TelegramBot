import config
import logging
# github sjekking
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#client part
@dp.message_handler(commands=['start', 'help',])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ha en god dag')

# echo
@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Hei':
        await message.answer('Hei til deg også!')




# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

