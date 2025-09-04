from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from db.add import AddDB
from db.search import SearchDB
from app.inline_button import app_menu_revers, back_menu


class Add_Finance(StatesGroup):
    waiting_category = State()
    waiting_sum = State()

@RouterStore.my_router.callback_query(CallbackDataFilter("add_category"))
async def add_category(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: add_category")
    await callback.answer()
    await callback.message.delete()
    await state.set_state(Add_Finance.waiting_category)
    await callback.message.answer("👉 Введите 📂 название категории расходов:",
                                  reply_markup=back_menu())
    

@RouterStore.my_router.message(Add_Finance.waiting_category)
async def add_sum_category(message: types.Message, state: FSMContext):
    if Read.search_symbol(message.text):
        await message.answer("👉 Прости я не умею работать с символом '_'\n"
                             "Придумай другое название")
    else:
        await state.update_data(category=message.text)
        await message.answer("👉 Укажите 💰 сумму, которую планируете потратить в этой категории:")
        LogCLassAll().debug(f"Write category: {message.text} user {message.from_user.id}")
        await state.set_state(Add_Finance.waiting_sum)
    
@RouterStore.my_router.message(Add_Finance.waiting_sum)
async def add_to_db(message: types.Message, state: FSMContext):
    LogCLassAll().debug(f"Write sum: {message.text} user {message.from_user.id}")
    data = await state.get_data()
    user_id = message.from_user.id
    category = data.get("category")
    image = types.FSInputFile('images/logo.png')
    test_double = await SearchDB().search_category_double(user_id, category)
    if await Read.checking_number(message.text):
        sum_money = round(float(message.text), 2)
        if test_double:
            await message.answer_photo(photo=image,
                            caption=f'*❌ Категория 📂{category} уже существует*',
                            parse_mode='Markdown',
                            reply_markup=app_menu_revers())
        else:
            AddDB().add_category_db(user_id=user_id,
                            category=category,
                            sum_money=sum_money)
            await state.clear()
            await message.answer_photo(photo=image,
                                    caption=f'*✅ Категория 📂{category} успешно добавлена*\n'
                                    f'*💵 Установлен лимит расходов для категории* _{sum_money}_',
                                    parse_mode='Markdown',
                                    reply_markup=app_menu_revers())
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
    