import logging
from web.main import RodinaHandler
from web.r import RequestsClient
from web.urls import urls
from aiogram.types import ReplyKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
API_TOKEN = '1626805312:AAE2uthUy5NTzMoi0vCxkvDECGHPobPmb5c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


keyboard_markup= InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Выставки",
                             callback_data='f')
        ],
        [
        InlineKeyboardButton(text="Кинцо",
                             callback_data='f')
        ]
    ]
)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Variki':
        answer = '''Hi! Какие варики конкретно интересуют братишка?'''
        await message.answer(answer, reply_markup=keyboard_markup)

    if message.text == 'Rodina':
        s = 'В родине варики такие, братишка'
        await message.answer('f', reply_markup=keyboard_markup)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

