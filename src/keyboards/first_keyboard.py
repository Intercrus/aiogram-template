from aiogram import types


first_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='First'),
            types.KeyboardButton(text='Second')
        ],
        [
            types.KeyboardButton(text='Third'),
        ],
    ],
    resize_keyboard=True
)
