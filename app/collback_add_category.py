from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from BaseClass.db_class import AddDB

class Add_Finance(StatesGroup):
    waiting_category = State()
    waiting_sum = State()

@RouterStore.my_router.callback_query(CallbackDataFilter("add_category"))
async def add_category(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: add_category")
    await callback.answer()
    await state.set_state(Add_Finance.waiting_category)
    await callback.message.answer("Введите название категории:")
    

@RouterStore.my_router.message(Add_Finance.waiting_category)
async def add_sum_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer("Теперь введите сумму которую хотите потратить для этой  категории:")
    LogCLassAll().debug(f"Write category: {message.text} user {message.from_user.id}")
    await state.set_state(Add_Finance.waiting_sum)
    
@RouterStore.my_router.message(Add_Finance.waiting_sum)
async def add_to_db(message: types.Message, state: FSMContext):
    LogCLassAll().debug(f"Write sum: {message.text} user {message.from_user.id}")
    data = await state.get_data()
    user_id = message.from_user.id
    category = data.get("category")
    print(category)
    sum_money = int(message.text)
    db = AddDB()
    db.add_category_db(user_id=user_id,
                       category=category,
                       sum_money=sum_money)
    await state.clear()
    await message.answer(f'Добавлена категоря: {category} \n'
                         f'С суммой для трат: {sum_money}')
    
    
    