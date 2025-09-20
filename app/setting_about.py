from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from app.inline_back import back_setting
from BaseClass.read_class import Images, Read

image_logo = Images.logo()

async def about(callback: types.CallbackQuery, parameter: str):
    LogCLassAll().debug(f"Started about function parameter: {parameter}")
    await callback.message.edit_media(media=types.InputMediaPhoto(
        media=image_logo, 
        caption=Read.read_txt(f'text/{parameter}.txt')),
        reply_markup=back_setting()
    )

@RouterStore.my_router.callback_query(CallbackDataFilter("update_period_about"))
async def update_period_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: update_period_about")
    await about(callback, "update_period_about")
    
@RouterStore.my_router.callback_query(CallbackDataFilter("shared_expenses_about"))
async def shared_expenses_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: shared_expenses_about")
    await about(callback, "shared_expenses_about")
    
@RouterStore.my_router.callback_query(CallbackDataFilter("notification_about"))
async def notification_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: notification_about")
    await about(callback, "notification_about")

@RouterStore.my_router.callback_query(CallbackDataFilter("delete_account_about"))
async def delete_account_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: delete_account_about")
    await about(callback, "delete_account_about")