from aiogram import Bot, Dispatcher, executor, types
import random

import logging
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


symbol = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\''
number = '0123456789'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Рандом бот")

@dp.message_handler()
async def random_bot(message: types.Message):
    random_password = "random"
    
    await message.answer(random_password)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)