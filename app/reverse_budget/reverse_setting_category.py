from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from db.search import SearchDB
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.inline_button import revers_db_setting, categories, app_menu_revers
from db.update import UpdateDB

class Add_Finance(StatesGroup):
    waiting_change_category = State()
    waiting_change_sum = State()

@RouterStore.my_router.callback_query(CallbackDataFilter("change_category"))
async def change_category(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: change_category")
    await callback.answer()
    image = types.FSInputFile('images/logo.png')
    await callback.message.answer_photo(photo=image,
                                        caption='🗂️✨ «Выберите кнопку, чтобы навести порядок в своих запасах»\n\n'
                                        'Вы можете изменить название и сумму выбранной категории',
                                        reply_markup=revers_db_setting())
    
    
@RouterStore.my_router.callback_query(CallbackDataFilter("rename_category"))
async def add_spending_choice_category(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: rename_category")
    await callback.answer()
    if await SearchDB().search_user_in_reverse(callback.from_user.id):
        categories_map = await categories(callback.from_user.id, 'rename_category')
        await callback.message.answer('Выбери категорию',
                                    reply_markup=categories_map)
    else:
        await callback.message.answer("❌У вас пока нет ни одной категории 🗂️ \n"
                                      "➡️ Добавьте первую, чтобы начать!")
        
@RouterStore.my_router.callback_query(F.data.startswith("rename_category_"))
async def write_new_name_category(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[-1]
    LogCLassAll().debug(f"Choice category change: {category}")
    await state.update_data(category=category)
    await state.set_state(Add_Finance.waiting_change_category)
    await callback.message.edit_text(f"🗂️✏️ Введите новое название категории {category}")
    
@RouterStore.my_router.message(Add_Finance.waiting_change_category)
async def update_name_category(message: types.Message, state: FSMContext):
    LogCLassAll().debug("Rename category")
    if Read.search_symbol(message.text):
        await message.answer("👉 Прости я не умею работать с символом '_'\n"
                             "Придумай другое название")
    else:
        data = await state.get_data()
        user_id = message.from_user.id
        category = data['category']
        new_name = message.text
        image = types.FSInputFile('images/logo.png')
        await UpdateDB().update_name_category(user_id, category, new_name)
        await state.clear()
        await message.answer_photo(photo=image,
                                    caption=f'💎 Готово! Новое название категории "{new_name}" '
                                    f'уже вместо "{category}". ✨',
                                    reply_markup=app_menu_revers())
        
        
        
@RouterStore.my_router.callback_query(CallbackDataFilter("change_sum"))
async def change_sum(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: change_sum")
    await callback.answer()
    if await SearchDB().search_user_in_reverse(callback.from_user.id):
        categories_map = await categories(callback.from_user.id, 'change_sum')
        await callback.message.answer('Выбери категорию',
                                    reply_markup=categories_map)
    else:
        await callback.message.answer("❌У вас пока нет ни одной категории 🗂️ \n"
                                      "➡️ Добавьте первую, чтобы начать!")
        
@RouterStore.my_router.callback_query(F.data.startswith("change_sum_"))
async def write_new_sum(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[-1]
    LogCLassAll().debug(f"Choice sum category change: {category}")
    await state.update_data(category=category)
    await state.set_state(Add_Finance.waiting_change_sum)
    await callback.message.edit_text(f"🗂️✏️ Введите новую сумму для категории {category}")
    
@RouterStore.my_router.message(Add_Finance.waiting_change_sum)
async def update_sum_category(message: types.Message, state: FSMContext):
    LogCLassAll().debug("Start update sum category")
    data = await state.get_data()
    user_id = message.from_user.id
    category = data['category']
    new_sum = message.text
    image = types.FSInputFile('images/logo.png')
    if await Read.checking_number(new_sum):
        await UpdateDB().update_sum_category(user_id, category, new_sum)
        await message.answer_photo(photo=image,
                                    caption=f'💎 Готово! Новое сумма в категории "{new_sum}" \n'
                                    f'Станет доступна после обновления". ✨',
                                    reply_markup=app_menu_revers())
        await state.clear()
    else:
        if ',' in new_sum:
            new_sum += '\nпоменяйте , на .'
        await message.answer(f"🔢 Хм… тут должно быть число, а не заклинание 😅\n"
                             f"Вы ввели: {new_sum}")