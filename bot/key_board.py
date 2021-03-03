from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

kb_variki = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Кинцо', callback_data='film')
        ],
        [
            InlineKeyboardButton('Выставки', callback_data='exhibition')
        ]
    ]
)

kb_film = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Родина', callback_data='rodina')
        ]
    ]
)

kb_exhibition = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Галерея "Миф"', callback_data='mif')
        ],
        [
            InlineKeyboardButton('Манеж', callback_data='manege')
        ]
    ]
)
