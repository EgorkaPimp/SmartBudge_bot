from aiogram.filters import Command
from aiogram import types
from pip._internal.utils.misc import tabulate

from db.search_db import view_categories
from create_table import create_table
from inline_keyboard import categories

async def register_handlers(dp):
    dp.message.register(cmd_start, Command('start'))
    dp.message.register(cmd_add, Command('add'))
    dp.message.register(cmd_view, Command('view'))




async def cmd_start(message: types.Message):
    await message.answer('Тут мы будем вместе следить за тем что происходит с нашими деньгами\n'
                         'Сколько их осталось по каждой из категорий')
    print(message.from_user.id)

async def cmd_add(message: types.Message):
    await message.answer('Выбери категорию',
                         reply_markup=categories())


async def cmd_view(message: types.Message):
    map_plan = await view_categories()
    full_table = await create_table(map_plan)
    await message.answer(
        "*📊 Воть так:*\n" + full_table,
        parse_mode="MarkdownV2")

