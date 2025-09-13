from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram.types import InputMediaPhoto, FSInputFile
from aiogram import types
from BaseClass.read_class import Read
from app.inline_button import app_menu
from BaseClass.read_class import Images

image_logo = Images.logo()

@RouterStore.my_router.callback_query(CallbackDataFilter("press_menu"))
async def menu_app(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: press_menu")
    await callback.message.edit_media(
    media=InputMediaPhoto(media=image_logo, caption="Главное меню:"),
    reply_markup=app_menu(),
)