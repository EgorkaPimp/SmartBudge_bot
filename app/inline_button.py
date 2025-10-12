from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from BaseClass.log_class import LogCLassAll
from db_postgres.crud.expenses import get_expenses

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
                            url='https://github.com/EgorkaPimp/SmartBudge_bot'),
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

def setting_category():
    inline_kb_list = [
        [
            InlineKeyboardButton(text="🗂️✨ Название",
                              callback_data='rename_category'),
            InlineKeyboardButton(text="🎲💎 Сумма",
                              callback_data='change_sum'),
            InlineKeyboardButton(text="🗂️💀 Удалить",
                              callback_data='del_category')
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

def notification_status(status_notification: int, status_update: int):
    if status_notification == 0:
        button_notification = "Включить ежедневный оповещение"
        notification_callback = "up_notification"
    elif status_notification == 1:
        button_notification = "Выключить ежедневное оповещение"
        notification_callback = "down_notification"
    if status_update == 0:
        button_update = "Включить ежемесячное оповещение"
        update_callback = "up_update"
    elif status_update == 1:
        button_update = "Выключить ежемесячное оповещение"
        update_callback = "down_update"
    inline_kb_list = [
        [
            InlineKeyboardButton(text=button_notification,
                            callback_data=notification_callback)],
        [
            InlineKeyboardButton(text=button_update,
                            callback_data=update_callback)
        ],
        [
            InlineKeyboardButton(text="🔙⚙️ Вернться в настройки",
                            callback_data='settings')
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

async def categories(user_id: int, interceptor: str):
    LogCLassAll().debug(f"Start search category user: {user_id}")
    categories_db = await get_expenses(user_id=user_id)  
    inline_kb_list = []
    for cat in categories_db:
        format_key = []
        format_key.append(InlineKeyboardButton(text=f"✨{cat.category}",
                                               callback_data=f'{interceptor}_{cat.category}'))
        inline_kb_list.append(format_key)
    back = [InlineKeyboardButton(text="🔙 Вернуться",
                                callback_data='press_menu')]
    inline_kb_list.append(back)
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


    