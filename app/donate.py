from BaseClass.start_class import RouterStore, CallbackDataFilter
from aiogram import types

@RouterStore.my_router.callback_query(CallbackDataFilter("donate_project"))
async def donate_project(callback: types.CallbackQuery):
    await callback.answer()
    
    