from attr import s
from fsm import DataInput
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

from fsm import DataInput
from sqlighter import SQLighter
from function import password_random

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = SQLighter('db/database.db')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user_settings(message.from_user.id)
        await message.answer("Рандом бот")
    else:
        await DataInput.state_length.set()
        await message.answer("""
Введите какой розмер будет пароль
/cancel - Окончить генерацию паролей
        """)

@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
    results = db.user_settings(message.from_user.id)
    for result in results:
        await message.answer(f"""
1. Upper {password_random.int_in_str(result[2])}
2. Lower {password_random.int_in_str(result[3])}
3. Number {password_random.int_in_str(result[4])}
4. Symbol {password_random.int_in_str(result[5])}
        """)
        await message.answer(f"""
Вводить настройку в таком стиле:
Upper on/off
        """)
    await DataInput.state_settings.set()

@dp.message_handler(commands=['cancel'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Happy End")


@dp.message_handler(state=DataInput.state_settings)
async def edit_settings(message: types.Message, state: FSMContext):
    message_list = message.text.split(' ')
    if message_list[0].lower() == 'upper' or message_list[0].lower() == 'lower' or message_list[0].lower() == 'number' or message_list[0].lower() == 'symbol':
        result = password_random.str_in_int(message_list[1].lower())
        db.update_user_settings(message.from_user.id, message_list[0].lower(), result)
        results = db.user_settings(message.from_user.id)
        for result in results:
            await message.answer(f"""
1. Upper {password_random.int_in_str(result[2])}
2. Lower {password_random.int_in_str(result[3])}
3. Number {password_random.int_in_str(result[4])}
4. Symbol {password_random.int_in_str(result[5])}
            """)
        await message.answer(f"""
Вы успешно обновили настройки
/cancel - Окончить и сохранить настройку
        """)
    else:
        await message.answer(f"Настройка: {message_list[0]} не найдена")

@dp.message_handler(state=DataInput.state_length)
async def length_password(message: types.Message, state: FSMContext):
    message_list = message.text.split(' ')
    if isinstance(message_list[0], str):
        password = await password_random.generate_password(message.from_user.id, message_list[0])
    else:
        password = "Вы должны ввести число"
    await message.answer(password)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)