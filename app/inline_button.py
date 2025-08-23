from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def app_func():
    inline_kb_list = [
        [InlineKeyboardButton(text="Добавить категорию",
                              callback_data='add_category')],

        [InlineKeyboardButton(text="Узнать обо мне побольше",
                              callback_data='about')],

        [InlineKeyboardButton(text="My_Git 😺",
                              url='https://github.com/EgorkaPimp/home_bot')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)