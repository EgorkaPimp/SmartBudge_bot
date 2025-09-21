from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types, F
from BaseClass.read_class import Images, Read
from db_postgres.crud.shares import status_share_search
from db_postgres.crud.expenses import add_to_expenses
from app.inline_button import categories, app_menu
from app.inline_back import back_menu

image_logo = Images.add_spending()

class Add_Finance(StatesGroup):
    waiting_sum_spending  = State()

@RouterStore.my_router.callback_query(CallbackDataFilter("add_spending"))
async def add_spending(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: add_spending")
    await callback.answer()
    await callback.message.delete()
    
    master = await status_share_search(callback.from_user.id)
    if master:
        user_id = master.master_id
    else:
        user_id = callback.from_user.id
    
    map_category = await categories(user_id=user_id, interceptor="spending")
    await callback.message.answer('Выбери категорию',
                                    reply_markup=map_category)
    
@RouterStore.my_router.callback_query(F.data.startswith("spending_"))
async def write_spending_sum(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[-1]
    LogCLassAll().debug(f"Choice category: {category}")
    await state.update_data(category=category)
    await state.set_state(Add_Finance.waiting_sum_spending)
    await callback.message.edit_text(f"📊 Сколько монет положим в категорию: {category}? 🪙",
                                     reply_markup=back_menu())
    
@RouterStore.my_router.message(Add_Finance.waiting_sum_spending)
async def del_cat_inc(message: types.Message, state: FSMContext):
    LogCLassAll().debug("Add spending")
    
    data = await state.get_data()
    master = await status_share_search(message.from_user.id)
    if master:
        user_id = master.master_id
    else:
        user_id = message.from_user.id
    category = data['category']
    spending = message.text
    
    if await Read.checking_number(spending):
        new_db = await add_to_expenses(user_id=user_id,
                                    category=category,
                                    amount_to_add=float(spending))
        print(new_db)
        await message.answer_photo(photo=image_logo,
                                    caption=f'💎 Готово! Новый остаток {new_db.amount_expenses} '
                                    f'уже в категории {category}. ✨',
                                    reply_markup=app_menu())
        await state.clear()
    else:
        if ',' in spending:
            spending += '\nпоменяйте , на .'
        await message.answer(f"🔢 Хм… тут должно быть число, а не заклинание 😅\n"
                             f"Вы ввели: {spending}")
    
    