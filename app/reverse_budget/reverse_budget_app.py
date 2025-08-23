from aiogram import types
from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import SearchDB, AddDB

@RouterStore.my_router.callback_query(CallbackDataFilter("reverse_budget"))
async def reverse_budget(callback: types.CallbackQuery):
    LogCLassAll().debug("Press revers budget")
    await callback.answer()
    user_id = callback.from_user.id
    if SearchDB().search_user(user_id):
        type_budget = SearchDB().search_type_budget(user_id)
        if type_budget["reverse_budget"] == 1:
            await callback.message.answer("Это ваша категория")
        else:
            await callback.message.answer("Это не ваша категория")
    else:
        AddDB().add_user_type_budget(user_id, "reverse")
        
    
    