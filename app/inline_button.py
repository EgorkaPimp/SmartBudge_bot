from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def app_start():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="📋 Перейти в меню",
                              callback_data='press_menu'),
            InlineKeyboardButton(text="ℹ️ Узнать обо мне побольше",
                              callback_data='about')
        ],
        [
            InlineKeyboardButton(text="🐙 My_Git",
                            url='https://github.com/EgorkaPimp/home_bot'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def app_menu():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="➕✨ Добавить категорию",
                              callback_data='add_category'),
            InlineKeyboardButton(text="📝💸 Внести трату",
                              callback_data='add_spending')
        ],
        [
            InlineKeyboardButton(text="📊✅ Показать таблицу",
                              callback_data='show_table'),
            InlineKeyboardButton(text="✏️🔧 Изменить категорию",
                              callback_data='change_category')
        ],
        [
            InlineKeyboardButton(text="⚙️ Настройки",
                            callback_data='settings'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def back_menu():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🔙 Вернться в меню",
                              callback_data='back_menu')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)