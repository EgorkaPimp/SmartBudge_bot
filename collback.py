from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio

router = Router()
# stop_flag = asyncio.Event()

from db.search_db import search_sum, rewrite_sum

class Add_Finance(StatesGroup):
    waiting_exp = State()

def add_fin_callbacks(dp):
    dp.include_router(router)

@router.callback_query(F.data.startswith('add_exp_'))
async def add_exp(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[-1]
    await state.update_data(category=category)
    await state.set_state(Add_Finance.waiting_exp)
    await callback.message.edit_text(f"Введите сумму для {category}:")

@router.message(Add_Finance.waiting_exp)
async def del_cat_inc(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data['category']
    sum_write = message.text
    sum_money = search_sum(category)
    is_number = lambda value: True if str(value).lstrip('-').replace('.', '', 1).isdigit() else False
    if is_number(sum_write):
        new_sum = sum_money - float(sum_write)
        rewrite_sum(category, new_sum)
        await message.answer(f'В категории {category} теперь {int(new_sum)}')
        await state.clear()
    else:
        if ',' in sum_write:
            sum_write += '\nпоменяйте , на .'
        await message.answer(f"Введи число коректно! \n"
                             f"Вы ввели: {sum_write}")

