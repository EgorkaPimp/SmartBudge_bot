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

def setting():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🔄 Обновить период",
                              callback_data='update_period'),
            InlineKeyboardButton(text="ℹ️ Описание",
                              callback_data='update_period_about')
        ],
        [
            InlineKeyboardButton(text="🤝 Совместные траты",
                              callback_data='shared_expenses'),
            InlineKeyboardButton(text="ℹ️ Описание",
                              callback_data='shared_expenses_about')
        ],
        [
            InlineKeyboardButton(text="🔔 Оповещение",
                              callback_data='notification'),
            InlineKeyboardButton(text="ℹ️ Описание",
                              callback_data='notification_about')
        ],
        [
            InlineKeyboardButton(text="🗑️ Удалиться",
                              callback_data='delete_account'),
            InlineKeyboardButton(text="ℹ️ Описание",
                              callback_data='delete_account_about')
        ],
        [
            InlineKeyboardButton(text="🌀🏰 Вернуться в меню",
                            callback_data='press_menu'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def confirmation_deletion():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="Да",
                            callback_data='yes_delete'),
            InlineKeyboardButton(text="Нет",
                            callback_data='settings')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)