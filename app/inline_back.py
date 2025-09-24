from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_setting():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🔙⚙️ Вернуться в настройки",
                              callback_data='settings')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def back_menu():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🔙🏘 Вернуться в меню",
                              callback_data='press_menu')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def back_setting_category():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🔙⚙️ Вернуться в настройки",
                              callback_data='change_category')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def back_start():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🔙▶️Вернуться на старт",
                              callback_data='press_back_start')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)