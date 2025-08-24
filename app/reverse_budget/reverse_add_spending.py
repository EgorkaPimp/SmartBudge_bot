from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.inline_button import categories

class Add_Finance(StatesGroup):
    waiting_sum = State()

@RouterStore.my_router.callback_query(CallbackDataFilter("add_spending"))
async def add_spending(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: add_spending")
    await callback.answer()
    categories_map = await categories(callback.from_user.id)
    await callback.message.answer('Выбери категорию',
                         reply_markup=categories_map)
    
