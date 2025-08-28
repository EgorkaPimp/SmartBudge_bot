from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from aiogram import types
from app.inline_button import back_start
from app.handlers_base import cmd_start

@RouterStore.my_router.callback_query(CallbackDataFilter("about"))
async def about(callback: types.CallbackQuery):
    LogCLassAll().info("Showing information about me")
    await callback.answer()
    await callback.message.delete()
    image = types.FSInputFile('images/about.png')
    await callback.message.answer_photo(photo=image,
                                        caption=Read.read_txt('text/about.txt'), 
                                        parse_mode="Markdown",
                                        reply_markup=back_start())
    
@RouterStore.my_router.callback_query(CallbackDataFilter("back_start"))
async def back_start_call(callback: types.CallbackQuery):
    LogCLassAll().info("Press button: back_start")
    await callback.answer()
    await callback.message.delete()
    await cmd_start(callback)