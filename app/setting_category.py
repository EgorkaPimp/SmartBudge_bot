from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.inline_button import setting_category, categories
from db_postgres.crud.shares import master_slave
from db_postgres.crud.expenses import delete_expense, update_expenses_amount, update_expenses
from db_postgres.crud.plan_spending import delete_plan_spending, update_plan_spending, update_name_category
from app.inline_back import back_setting_category
from BaseClass.read_class import Images, Read

image_logo = Images.setting()  

class Add_Finance(StatesGroup):
    waiting_new_sum_spending  = State()  
    waiting_category_name = State()  

@RouterStore.my_router.callback_query(CallbackDataFilter("change_category"))
async def change_category(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: change_category")
    await callback.answer()
    await callback.message.edit_media(
    media=types.InputMediaPhoto(media=image_logo, 
                                caption='🗂️✨ «Выберите кнопку, чтобы навести порядок в своих запасах»\n\n'
                                        'Вы можете изменить название и сумму выбранной категори иили удалить категорию.\n'),
                                reply_markup=setting_category(),)
    
@RouterStore.my_router.callback_query(CallbackDataFilter("del_category"))
async def choice_category_del(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: choice_category_del")
    await callback.answer()
    await callback.message.delete()
    
    user_id = await master_slave(callback.from_user.id)
    
    map_category = await categories(user_id=user_id, interceptor="del_category_")
    await callback.message.answer('Выбери категорию',
                                    reply_markup=map_category)
    
@RouterStore.my_router.callback_query(F.data.startswith("del_category_"))
async def del_category(callback: types.CallbackQuery):
    category = callback.data.split("_")[-1]
    LogCLassAll().debug(f"Choice category: {category} for delete")
    await callback.message.delete()
    user_id = await master_slave(callback.from_user.id)
    await delete_expense(user_id=user_id,
                         category=category)
    await delete_plan_spending(user_id=user_id, 
                               category=category)
    await callback.message.answer_photo(photo=image_logo,
                                        caption=f"🗑️ Категория {category} была успешно удалена! ✅",
                                        reply_markup=setting_category())
    
@RouterStore.my_router.callback_query(CallbackDataFilter("change_sum"))
async def choice_change_sum(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: choice_change_sum")
    await callback.answer()
    await callback.message.delete()
    
    user_id = await master_slave(callback.from_user.id)
    
    map_category = await categories(user_id=user_id, interceptor="change_category_")
    await callback.message.answer('Выбери категорию',
                                    reply_markup=map_category)
    
@RouterStore.my_router.callback_query(F.data.startswith("change_category_"))
async def change_sum(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[-1]
    LogCLassAll().debug(f"Choice category: {category} for change sum")
    await state.update_data(category=category)
    await state.set_state(Add_Finance.waiting_new_sum_spending)
    await callback.message.edit_text(f"📊 Сколько монет положим в категорию: {category}? 🪙",
                                     reply_markup=back_setting_category())
    
@RouterStore.my_router.message(Add_Finance.waiting_new_sum_spending)
async def change_sum_in_db(message: types.Message, state: FSMContext):
    LogCLassAll().debug("Add change_sum")
    
    data = await state.get_data()
    user_id = await master_slave(message.from_user.id)
    category = data['category']
    spending = message.text
    
    if await Read.checking_number(spending):
        new_exp = await update_plan_spending(user_id=user_id,
                                   category=category,
                                   new_amount=float(spending))
        
        await update_expenses_amount(user_id=user_id,
                                     category=category,
                                     new_amount=new_exp)
        
        await message.answer_photo(photo=image_logo,
                                    caption='💰 Новая сумма успешно добавлена в план!\n'
                                            '📊 Таблица уже обновлена и отображается с учётом перерасчёта ✨',
                                    reply_markup=setting_category())
        await state.clear()
    else:
        if ',' in spending:
            spending += '\nпоменяйте , на .'
        await message.answer(f"🔢 Хм… тут должно быть число, а не заклинание 😅\n"
                             f"Вы ввели: {spending}")
    
@RouterStore.my_router.callback_query(CallbackDataFilter("rename_category"))
async def rename_category_choice(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: rename_category_choice")
    await callback.answer()
    await callback.message.delete()
    
    user_id = await master_slave(callback.from_user.id)
    
    map_category = await categories(user_id=user_id, interceptor="new_name_")
    await callback.message.answer('Выбери категорию',
                                    reply_markup=map_category)
    
@RouterStore.my_router.callback_query(F.data.startswith("new_name_"))
async def add_category(callback: types.CallbackQuery, state: FSMContext):
        category = callback.data.split("_")[-1]
        await state.update_data(category=category)
        LogCLassAll().debug("Press button: rename")
        await callback.answer()
        await callback.message.edit_text("👉 Введите 📂 название категории расходов:",
                                  reply_markup=back_setting_category())
        await state.set_state(Add_Finance.waiting_category_name)
    
@RouterStore.my_router.message(Add_Finance.waiting_category_name)
async def add_sum_category(message: types.Message, state: FSMContext):
        if Read.search_symbol(message.text):
                await message.edit_text("👉 Прости я не умею работать с символом '_'\n"
                             "Придумай другое название")
        else:
                data = await state.get_data()
                user_id = await master_slave(message.from_user.id)
                category = data['category']
                await update_expenses(user_id=user_id,
                                      category=category,
                                      new_category=message.text)
                
                await update_name_category(user_id=user_id,
                                        category=category,
                                        new_name=message.text)
                await message.answer_photo(photo=image_logo,
                                    caption=f'✏️ Категория {category} успешно переименована в {message.text}! ✅',
                                    reply_markup=setting_category())
                await state.clear()
                
                
                
                
            