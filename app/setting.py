from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram.fsm.context import FSMContext
from aiogram import types
from app.inline_button import setting
from BaseClass.read_class import Images

image_logo = Images.logo()

@RouterStore.my_router.callback_query(CallbackDataFilter("settings"))
async def settings(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: settings")
    await callback.message.edit_media(
    media=types.InputMediaPhoto(media=image_logo, caption="Главное меню:"),
    reply_markup=setting(),
    )
    