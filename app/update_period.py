from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from app.inline_button import setting
from BaseClass.read_class import Images
from db_postgres.crud.utils import sync_expenses_with_plans, get_category_comparison
from db_postgres.crud.shares import master_slave, search_slave
from db_postgres.crud.status_scheduler import update_status_scheduler
from db_postgres.crud.every_waste import delete_update
from app.show_table import create_table
from BaseClass.json_class import JsonWork

image_logo = Images.setting()

@RouterStore.my_router.callback_query(CallbackDataFilter("update_period"))
async def update_period(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: update_period")
    user_id = await master_slave(callback.from_user.id)
    if user_id == callback.from_user.id:
        await callback.message.delete()
        
        plan = await get_category_comparison(user_id=user_id)
        full_table = await create_table(plan)
        slave = await search_slave(user_id=user_id)
        
        """Создание отчета json"""
        worker = await JsonWork.create(user_id=user_id)
        await worker.to_json()
        await worker.save(f"report_{worker.user_id}")
        
        """Удалить каждую трату после формирования отчета"""
        await delete_update(user_id=user_id)
        
                   
        await callback.message.answer(text="📊📊Вот так выглядит твой месяц:📊📊\n" + full_table,
                                        parse_mode="MarkdownV2",)
        
        if slave:
            slave = slave.slave_id
            await update_status_scheduler(user_id=slave,
                                      new_status=0,
                                      type_status='status_update')
            await callback.bot.send_message(chat_id=slave,
                                               text="Вот так выглядит твой месяц:\n" + full_table,
                                               parse_mode="MarkdownV2")
            
        
        await sync_expenses_with_plans(user_id=callback.from_user.id)
        
        await update_status_scheduler(user_id=callback.from_user.id,
                                      new_status=0,
                                      type_status='status_update')
        
        
        await callback.message.answer_photo(photo=image_logo, 
                                            caption="✅Вы успешно обновили период.✅\n\n"
                                            "⚠️Обновление 1 чмсла отменено⚠️\n",
                                            parse_mode="Markdown",
                                            reply_markup=setting())
    else:
        await callback.message.edit_media(media=types.InputMediaPhoto(
            media=image_logo, 
            caption="❌Вы подключены к таблици другого человека, попросите его обновить период❌",
            parse_mode="Markdown"),
            reply_markup=setting())
    