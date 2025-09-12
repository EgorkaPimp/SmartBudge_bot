from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from BaseClass.read_class import Read
from app.inline_button import confirmation_deletion
from db.delete import DeleteDB

@RouterStore.my_router.callback_query(CallbackDataFilter("shared_expenses"))
async def delete_account(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: shared_expenses")
    