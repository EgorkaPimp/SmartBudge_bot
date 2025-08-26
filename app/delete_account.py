from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from BaseClass.read_class import Read
from app.inline_button import confirmation_deletion

@RouterStore.my_router.callback_query(CallbackDataFilter("delete_account"))
async def delete_account(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: delete_account")
    await callback.answer()
    await callback.message.answer(Read.read_txt('text/delete_account.txt'),
                                  message_effect_id="5046589136895476101",
                                  reply_markup=confirmation_deletion())