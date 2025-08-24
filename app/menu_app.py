from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from BaseClass.start_class import InstanceBot
from app.inline_button import app_menu, app_menu_revers
from BaseClass.read_class import Read
from db.search import SearchDB

@RouterStore.my_router.callback_query(CallbackDataFilter("press_menu"))
async def pres_menu(callback: types.CallbackQuery):
    LogCLassAll().debug("callback 'menu' press")
    await callback.answer()
    await menu(callback.from_user.id)
     
async def menu(chat: int):
    LogCLassAll().debug("function 'menu' started correct")
    image = types.FSInputFile('images/logo.png')
    if SearchDB().search_user(chat):
        type_budget = SearchDB().search_type_budget(chat)
        if type_budget["reverse_budget"] == 1:
            await InstanceBot.bot.send_photo(chat_id=chat,
                                            photo=image,
                                            caption='*Обратный бюджет*',
                                            parse_mode='Markdown',
                                            reply_markup=app_menu_revers())
    else:
        await InstanceBot.bot.send_photo(chat_id=chat,
                                        photo=image,
                                        caption="*Меню:* выбери категорию", 
                                        parse_mode="Markdown",
                                        reply_markup=app_menu())
    
@RouterStore.my_router.callback_query(CallbackDataFilter("reverse_budget_about"))
async def reverse_budget_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press about revers budget")
    await callback.answer()
    await callback.message.answer(Read.read_txt('text/reverse_budget.txt'))
    
@RouterStore.my_router.callback_query(CallbackDataFilter("financial_diary_about"))
async def financial_diary_about(callback: types.CallbackQuery):
    LogCLassAll().debug("Press about financial_diary_about budget")
    await callback.answer()
    await callback.message.answer(Read.read_txt('text/financial_diary.txt'))
    
@RouterStore.my_router.callback_query(CallbackDataFilter("financial_diary"))
async def financial_diary(callback: types.CallbackQuery):
    LogCLassAll().debug("Press financial diary")
    await callback.answer()
    await callback.message.answer("🙌🏻*Приношу свои извенеения*\n\n"
                                "🥺К сожелению данная функция находиться в разработке\n\n"
                                "🫡Я уже тружуусь что бы все исправить!",
                                parse_mode="Markdown")