from BaseClass.start_class import RouterStore
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram import types
from BaseClass.log_class import LogCLassAll
from app.inline_button import app_start
from app.menu_app import menu

@RouterStore.my_router.message(Command("start"))
async def cmd_start(event: types.Message | types.CallbackQuery):
    LogCLassAll().debug('handler "start" write')
    if isinstance(event, types.CallbackQuery):
        chat_id = event.message.chat.id
    else:
        await event.delete()
        chat_id = event.chat.id

    image = FSInputFile('images/welcome.jpg')
    await event.bot.send_photo(
        chat_id=chat_id,
        photo=image,
        reply_markup=app_start()
    )
    
@RouterStore.my_router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    LogCLassAll().debug('handler "menu" write')
    await message.delete()
    await menu(message.chat.id)