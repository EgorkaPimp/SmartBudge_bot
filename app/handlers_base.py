from BaseClass.start_class import RouterStore
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram import types
from BaseClass.log_class import LogCLassAll
from app.inline_button import app_start
from app.menu_app import menu

@RouterStore.my_router.message(Command("start"))
async def  cmd_start(message: types.Message):
    LogCLassAll().debug('handler "star" write')
    image = FSInputFile('images/welcome.jpg')
    await message.answer_photo(photo=image,
                               reply_markup=app_start())
    
@RouterStore.my_router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    LogCLassAll().debug('handler "menu" write')
    await menu(message.chat.id)