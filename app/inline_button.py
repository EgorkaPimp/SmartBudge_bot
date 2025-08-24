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
            InlineKeyboardButton(text="💰 Обратный бюджет",
                              callback_data='reverse_budget'),
            InlineKeyboardButton(text="ℹ️ Описание",
                              callback_data='reverse_budget_about')
        ],
        [
            InlineKeyboardButton(text="📔 Финансовый дневник",
                              callback_data='financial_diary'),
            InlineKeyboardButton(text="ℹ️ Описание",
                              callback_data='financial_diary_about')
        ],
        [
            InlineKeyboardButton(text="⚙️ Настройки",
                            callback_data='settings'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def app_menu_revers():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="➕✨ Добавить категорию",
                              callback_data='reverse_budget'),
            InlineKeyboardButton(text="📝💸 Внести трату",
                              callback_data='reverse_budget_about')
        ],
        [
            InlineKeyboardButton(text="📊✅ Показать таблицу",
                              callback_data='financial_diary'),
            InlineKeyboardButton(text="✏️🔧 Изменить категорию",
                              callback_data='financial_diary_about')
        ],
        [
            InlineKeyboardButton(text="⚙️ Настройки",
                            callback_data='settings'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)