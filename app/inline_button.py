from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def app_func():
    inline_kb_list = [
        [InlineKeyboardButton(text="Добавить категорию",
                              callback_data='add_category')],

        [InlineKeyboardButton(text="Показать категории",
                              callback_data='delete_user')],
        
        [InlineKeyboardButton(text="Показать таблицу",
                              callback_data='delete_user')],

        [InlineKeyboardButton(text="My_Git 😺",
                              url='https://github.com/EgorkaPimp/home_bot')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)