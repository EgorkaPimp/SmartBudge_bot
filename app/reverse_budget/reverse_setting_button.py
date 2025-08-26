from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from aiogram import types
from app.inline_button import revers_setting, back_setting

@RouterStore.my_router.callback_query(CallbackDataFilter("settings"))
async def settings(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: settings")
    await callback.answer()
    image = types.FSInputFile('images/logo.png')
    await callback.message.answer_photo(photo=image,
                                        caption='⚙️ Настройки \n'
                                        'Здесь вы можете изменить параметры для удобства использования:',
                                        reply_markup=revers_setting())
    
async def about(callback: types.CallbackQuery, parameter: str):
    LogCLassAll().debug(f"Started about function parameter: {parameter}")
    image = types.FSInputFile('images/logo.png')
    await callback.message.answer_photo(photo=image,
                                        caption=Read.read_txt(f'text/{parameter}.txt'), 
                                        parse_mode="Markdown",
                                        reply_markup=back_setting())
    
@RouterStore.my_router.callback_query(CallbackDataFilter("update_period_about"))
async def update_period_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: update_period_about")
    await callback.answer()
    await about(callback, "update_period_about")
    
@RouterStore.my_router.callback_query(CallbackDataFilter("shared_expenses_about"))
async def shared_expenses_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: shared_expenses_about")
    await callback.answer()
    await about(callback, "shared_expenses_about")
    
@RouterStore.my_router.callback_query(CallbackDataFilter("notification_about"))
async def notification_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: notification_about")
    await callback.answer()
    await about(callback, "notification_about")

@RouterStore.my_router.callback_query(CallbackDataFilter("delete_account_about"))
async def delete_account_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: delete_account_about")
    await callback.answer()
    await about(callback, "delete_account_about")
    
@RouterStore.my_router.callback_query(CallbackDataFilter("back_setting"))
async def back_setting_callback(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: back_setting")
    await callback.answer()
    await settings(callback)


    