from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from app.inline_button import setting, confirmation_deletion
from BaseClass.read_class import Images, Read
from db_postgres.crud.users import delete_user

image_logo = Images.setting()
image_logo_start = Images.welcome_image()

@RouterStore.my_router.callback_query(CallbackDataFilter("settings"))
async def settings(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: settings")
    await callback.message.edit_media(
    media=types.InputMediaPhoto(media=image_logo, caption="Главное меню:"),
    reply_markup=setting(),
    )
    
"""----------------Delete acount from db---------------------"""

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
    await delete_user(callback.from_user.id)
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer_photo(photo=image_logo_start,
                                        caption='Мне очень жадь что ты больше не считаешь свои расходы! \n'
                                        'Буду рад видеть тебя снова')
    
"""-----------------------------------------------------------"""
    
                                        
