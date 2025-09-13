from BaseClass.start_class import RouterStore
from aiogram.filters import Command
from aiogram import types
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Images, Text
from db_postgres.crud.users import add_user
from db_postgres.crud.reminders import add_reminders
from db_postgres.crud.status_scheduler import add_status_scheduler
from app.inline_button import app_start

welcome_image = Images.welcome_image()
welcome_text = Text.welcome_text

@RouterStore.my_router.message(Command("start"))
async def cmd_start(message: types.Message | types.CallbackQuery):
    LogCLassAll().debug('handler "start" write')
    
    if await add_user(user_id=message.chat.id,
                   username=message.chat.username):
        
        await add_reminders(user_id=message.chat.id)
        await add_status_scheduler(user_id=message.chat.id)
        
    await message.answer_photo(photo=welcome_image,
                            caption=welcome_text,
                            message_effect_id = '5046509860389126442',
                            reply_markup = app_start())