from BaseClass.start_class import RouterStore
from aiogram.filters import Command, CommandObject
from aiogram import types
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Images, Text, Generate
from db_postgres.crud.users import add_user
from db_postgres.crud.reminders import add_reminders
from db_postgres.crud.status_scheduler import add_status_scheduler
from app.inline_button import app_start
from db_postgres.crud.shares import status_share_search, add_share_status_slave

welcome_image = Images.welcome_image()
welcome_text = Text.welcome_text

@RouterStore.my_router.message(Command("start"))
async def cmd_start(message: types.Message, command: CommandObject):
    if await add_user(user_id=message.chat.id,
                username=message.chat.username):
        
        await add_reminders(user_id=message.chat.id)
        await add_status_scheduler(user_id=message.chat.id)
    if command.args:
        args = command.args
        if args.startswith("share_"):
            LogCLassAll().debug('handler "start" write with link for user')
            ref_id = await Generate.encode_user_id(payload = args.split("_", 1)[1])
            if not await status_share_search(user_id=message.chat.id):
                await add_share_status_slave(user_id=message.chat.id,
                                            master_id=ref_id)

    else:
        LogCLassAll().debug('handler "start" write')
            
    await message.answer_photo(photo=welcome_image,
                            caption=welcome_text,
                            message_effect_id = '5046509860389126442',
                            reply_markup = app_start())