from aiogram import types
from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from db.search import SearchDB
from db.add import AddDB
from app.inline_button import app_menu_revers

@RouterStore.my_router.callback_query(CallbackDataFilter("reverse_budget"))
async def reverse_budget(callback: types.CallbackQuery):
    LogCLassAll().debug("Press revers budget")
    await callback.answer()
    user_id = callback.from_user.id
    image = types.FSInputFile('images/logo.png')
    if not SearchDB().search_user(user_id):
        AddDB().add_user_type_budget(user_id, "reverse")
    type_budget = SearchDB().search_type_budget(user_id)
    if type_budget["reverse_budget"] == 1:
        await callback.message.answer_photo(photo=image,
                                            caption='*Обратный бюджет*',
                                            parse_mode='Markdown',
                                            reply_markup=app_menu_revers())
    else:
        await callback.message.answer("Это не ваша категория")
        
