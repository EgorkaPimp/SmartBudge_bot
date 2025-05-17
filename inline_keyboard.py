from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from db.search_db import search_cat

def categories():
    categories = search_cat()
    inline_kb_list = []
    for cat in categories:
        format_key = []
        format_key.append(InlineKeyboardButton(text=f"{cat[0].capitalize()}",
                                               callback_data=f'add_exp_{cat[0].capitalize()}'))
        inline_kb_list.append(format_key)
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)