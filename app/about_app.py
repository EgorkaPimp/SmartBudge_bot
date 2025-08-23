from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from aiogram import types

@RouterStore.my_router.callback_query(CallbackDataFilter("about"))
async def about(callback: types.CallbackQuery):
    LogCLassAll().info("Showing information about me")
    await callback.answer()
    await callback.message.answer(Read.read_txt('text/about.txt'), 
                                  parse_mode="Markdown")