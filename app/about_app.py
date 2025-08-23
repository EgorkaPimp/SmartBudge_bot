from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from BaseClass.read_class import Read
from aiogram import types

@RouterStore.my_router.callback_query(CallbackDataFilter("about"))
async def about(callback: types.CallbackQuery):
    LogCLassAll().info("Showing information about me")
    await callback.answer()
    image = types.FSInputFile('images/about.png')
    await callback.message.answer_photo(photo=image,
                                        caption=Read.read_txt('text/about.txt'), 
                                        parse_mode="Markdown")