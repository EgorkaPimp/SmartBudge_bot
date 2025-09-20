from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from app.inline_button import notification_status
from BaseClass.read_class import Images, Read
from db_postgres.crud.status_scheduler import search_status, update_status_scheduler

image_logo = Images.logo()

@RouterStore.my_router.callback_query(CallbackDataFilter("notification"))
async def notification(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: notification")
    await callback.answer()
    status = await search_status(user_id = callback.from_user.id)
    if status.status_notification == 1:
        message_notification = '✅Вы получаете оповещение каждый день в 22:45✅'
    elif status.status_notification == 0:
        message_notification = '❌Вы не получаете оповещение каждый день в 22:45❌'
    if status.status_update == 1:
        message_update = '✅Ваш перод трат обновиться 1 числа в 10:00✅'
    elif status.status_update == 0:
        message_update = '❌Ваш перод трат не обновиться 1 числа в 10:00❌'
    
    await callback.message.edit_media(media=types.InputMediaPhoto(
            media=image_logo, 
            caption="*Вот так выглядят ваши настройки оповещения:*\n\n"
                    "_Ежедневные:_ \n"
                    f"{message_notification}\n\n"
                    "_Ежемесячные:_ \n"
                    f"{message_update}",
            parse_mode="Markdown"),
            reply_markup=notification_status(status_notification=status.status_notification,
                                             status_update=status.status_update)
        )

    
@RouterStore.my_router.callback_query(CallbackDataFilter("up_notification"))
async def up_notification(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: up_notification")
    await update_status_scheduler(user_id=callback.from_user.id,
                                  new_status=1,
                                  type_status="status_notification")
    await notification(callback)
    
@RouterStore.my_router.callback_query(CallbackDataFilter("down_notification"))
async def down_notification(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: down_notification")
    await update_status_scheduler(user_id=callback.from_user.id,
                                  new_status=0,
                                  type_status="status_notification")
    await notification(callback)
    
@RouterStore.my_router.callback_query(CallbackDataFilter("up_update"))
async def up_update(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: up_update")
    await update_status_scheduler(user_id=callback.from_user.id,
                                  new_status=1,
                                  type_status="status_update")
    await notification(callback)
    
@RouterStore.my_router.callback_query(CallbackDataFilter("down_update"))
async def down_update(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: down_update")
    await update_status_scheduler(user_id=callback.from_user.id,
                                  new_status=0,
                                  type_status="status_update")
    await notification(callback)