from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from BaseClass.read_class import Read
from app.inline_button import confirmation_deletion
from db.delete import DeleteDB

@RouterStore.my_router.callback_query(CallbackDataFilter("delete_account"))
async def delete_account(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: delete_account")
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(Read.read_txt('text/delete_account.txt'),
                                  message_effect_id="5046589136895476101",
                                  reply_markup=confirmation_deletion())
    
@RouterStore.my_router.callback_query(CallbackDataFilter("yes_delete"))
async def yes_delete(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: yes_delete")
    await DeleteDB().delete_user(callback.from_user.id)
    await callback.answer()
    await callback.message.delete()
    image = types.FSInputFile('images/logo.png')
    await callback.message.answer_photo(photo=image,
                                        caption='Мне очень жадь что ты больше не считаешь свои расходы! \n'
                                        'Буду рад вмдеть тебя снова')
