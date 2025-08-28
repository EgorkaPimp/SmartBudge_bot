from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.inline_button import categories, app_menu_revers, back_menu
from db.search import SearchDB
from db.update import UpdateDB

class Add_Finance(StatesGroup):
    waiting_sum_spending = State()
    

@RouterStore.my_router.callback_query(CallbackDataFilter("add_spending"))
async def add_spending_choice_category(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: add_spending")
    await callback.answer()
    await callback.message.delete()
    if await SearchDB().search_user_in_reverse(callback.from_user.id):
        categories_map = await categories(callback.from_user.id, "spending")
        await callback.message.answer('Выбери категорию',
                                    reply_markup=categories_map)
    else:
        await callback.message.answer("❌У вас пока нет ни одной категории 🗂️ \n"
                                      "➡️ Добавьте первую, чтобы начать!")
    
    
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
    user_id = message.from_user.id
    category = data['category']
    spending = message.text
    old_sum_db = await SearchDB().search_sum_in_reverse_budget(user_id, category)
    image = types.FSInputFile('images/logo.png')
    if await Read.checking_number(spending):
        new_sum = old_sum_db - float(spending)
        await UpdateDB().update_sum_reverse_budget(user_id, category, new_sum)
        await message.answer_photo(photo=image,
                                   caption=f'💎 Готово! Новый остаток {new_sum} '
                                   f'уже в категории {category}. ✨',
                                   reply_markup=app_menu_revers())
        await state.clear()        
    else:
        if ',' in spending:
            spending += '\nпоменяйте , на .'
        await message.answer(f"🔢 Хм… тут должно быть число, а не заклинание 😅\n"
                             f"Вы ввели: {spending}")