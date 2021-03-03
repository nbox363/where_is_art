import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text

from key_board import kb_variki, kb_film, kb_exhibition
from bot import Helper

API_TOKEN = '1626805312:AAE2uthUy5NTzMoi0vCxkvDECGHPobPmb5c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

help_message = text(
    "Доступные команды:\n",
    "/variki - какие варики",
    sep="\n"
)

helper = Helper()


@dp.message_handler(commands=['help', 'start'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


@dp.message_handler(commands=['variki'])
async def process_variki(message: types.Message):
    await message.reply("Здорово, долбоеб!\n Какие варики конкретно интересуют, братишка?", reply_markup=kb_variki)



### Films ###
@dp.callback_query_handler(lambda c: c.data == 'film')
async def process_callback_film(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'По кинцу варики такие, братишка', reply_markup=kb_film)


# Rodina
@dp.callback_query_handler(lambda c: c.data == 'rodina')
async def process_callback_rodina(callback_query: types.CallbackQuery):
    sessions = helper.film(callback_query.data).get()
    answer = '''В Родине варике такие, братишка \n\n'''
    for i, session in enumerate(sessions):
        answer += str(session) + '\n\n'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, answer)


### Exhibition ###
@dp.callback_query_handler(lambda c: c.data == 'exhibition')
async def process_callback_exhibition(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'По выставкам вариков не дохуя', reply_markup=kb_exhibition)


# Mif #
@dp.callback_query_handler(lambda c: c.data == 'mif')
async def process_callback_mif(callback_query: types.CallbackQuery):
    sessions = helper.e(callback_query.data).get()
    answer = '''Такой варик'''
    for i, session in enumerate(sessions):
        answer += str(session) + '\n\n'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, answer)


# Manege #
@dp.callback_query_handler(lambda c: c.data == 'manege')
async def process_callback_button1(callback_query: types.CallbackQuery):
    # sessions = helper.e(callback_query.data).get()
    answer = '''Такой варик'''
    # for i, session in enumerate(sessions):
    #     answer += str(session) + '\n\n'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
