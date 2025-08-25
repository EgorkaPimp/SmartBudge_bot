from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.search import SearchDB
from BaseClass.log_class import LogCLassAll

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


async def categories(user_id: int, interceptor: str):
    LogCLassAll().debug(f"Start search category user: {user_id}")
    categories = await SearchDB().search_category_table(user_id)
    inline_kb_list = []
    for cat in categories:
        format_key = []
        format_key.append(InlineKeyboardButton(text=f"{cat[0].capitalize()}",
                                               callback_data=f'{interceptor}_{cat[0].capitalize()}'))
        inline_kb_list.append(format_key)
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def revers_db_setting():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🗂️✨ Категория",
                              callback_data='rename_category'),
            InlineKeyboardButton(text="🎲💎 Подкрутить сумму",
                              callback_data='change_sum')
        ],
        [
            InlineKeyboardButton(text="🌀🏰 Вернуться в меню",
                            callback_data='back_menu'),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)