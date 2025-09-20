from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types
from BaseClass.read_class import Read
from app.inline_button import app_menu
from app.inline_back import back_menu
from BaseClass.read_class import Images
from db_postgres.crud.expenses import add_expense, category_exists
from db_postgres.crud.plan_spending import add_plan_spending
from db_postgres.crud.shares import status_share_search

image_logo = Images.logo()

class Add_Finance(StatesGroup):
    waiting_category = State()
    waiting_sum = State()

@RouterStore.my_router.callback_query(CallbackDataFilter("add_category"))
async def add_category(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: add_category")
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("👉 Введите 📂 название категории расходов:",
                                  reply_markup=back_menu())
    await state.set_state(Add_Finance.waiting_category)
    
@RouterStore.my_router.message(Add_Finance.waiting_category)
async def add_sum_category(message: types.Message, state: FSMContext):
    if Read.search_symbol(message.text):
        await message.answer("👉 Прости я не умею работать с символом '_'\n"
                             "Придумай другое название")
    else:
        if not await category_exists(user_id=message.from_user.id,
                           category=message.text):
            await state.update_data(category=message.text)
            await message.answer("👉 Укажите 💰 сумму, которую планируете потратить в этой категории:")
            LogCLassAll().debug(f"Write category: {message.text} user {message.from_user.id}")
            await state.set_state(Add_Finance.waiting_sum)
        else:
            await message.answer(f'❌ Категория 📂{message.text} уже существует\n'
                                 'Введите название еще раз')
        
@RouterStore.my_router.message(Add_Finance.waiting_sum)
async def add_to_db(message: types.Message, state: FSMContext):
    LogCLassAll().debug(f"Write sum: {message.text} user {message.from_user.id}")
    data = await state.get_data()
    master = await status_share_search(message.from_user.id)
    if master:
        user_id = master.master_id
    else:
        user_id = message.from_user.id
    category = data.get("category")
    if await Read.checking_number(message.text):
        sum_money = round(float(message.text), 2)
        await add_plan_spending(user_id=user_id,
                        category=category,
                        amount_money=sum_money)
        await add_expense(user_id=user_id,
                    category=category,
                    amount_expenses=sum_money)
        await message.answer_photo(photo=image_logo,
                        caption=f'*✅ Категория 📂{category} добавлена*\n'
                        f'Запланированая сумма 💰= {sum_money}',
                        parse_mode='Markdown',
                        reply_markup=app_menu())
        await state.clear()
    else:
        if any(ch.isalpha() for ch in message.text):
             await message.answer(f"🔢 Хм… тут должно быть число, а не заклинание 😅\n"
                                f"Вы ввели: {message.text}\n"
                                "Введите число повторно")
        if ',' in message.text:
            await message.answer(f"🔢 Хм… тут должно быть число, а не заклинание 😅\n"
                                    f"Вы ввели: {message.text} \n"
                                    "Возможно надо поменять , на .\n"
                                    "Введите число повторно")