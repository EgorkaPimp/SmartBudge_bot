from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from app.inline_button import setting_category
from BaseClass.read_class import Images

image_logo = Images.logo()

@RouterStore.my_router.callback_query(CallbackDataFilter("change_category"))
async def change_category(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: change_category")
    await callback.answer()
    await callback.message.edit_media(
    media=types.InputMediaPhoto(media=image_logo, 
                                caption='🗂️✨ «Выберите кнопку, чтобы навести порядок в своих запасах»\n\n'
                                        'Вы можете изменить название и сумму выбранной категори иили удалить категорию.\n'),
                                reply_markup=setting_category(),)