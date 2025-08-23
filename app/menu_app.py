from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from BaseClass.start_class import InstanceBot
from app.inline_button import app_menu

@RouterStore.my_router.callback_query(CallbackDataFilter("press_menu"))
async def pres_menu(callback: types.CallbackQuery):
    LogCLassAll().debug("callback 'menu' press")
    await callback.answer()
    await menu(callback.from_user.id)
     
async def menu(chat: int):
    LogCLassAll().debug("function 'menu' started correct")
    image = types.FSInputFile('images/logo.png')
    await InstanceBot.bot.send_photo(chat_id=chat,
                                    photo=image,
                                    caption="*Меню:* выбери категорию", 
                                    parse_mode="Markdown",
                                    reply_markup=app_menu())