from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram.fsm.context import FSMContext
from aiogram import types
from app.inline_back import back_setting
from BaseClass.read_class import Images, Generate
from db_postgres.crud.shares import add_share_status_master, status_share_search

image_logo = Images.logo()

@RouterStore.my_router.callback_query(CallbackDataFilter("shared_expenses"))
async def shared_expenses(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: shared_expenses")
    await callback.answer()
    if not await status_share_search(user_id=callback.from_user.id):
        link = await Generate.generate_link(callback.from_user.id)
        await add_share_status_master(user_id=callback.from_user.id)
        await callback.message.edit_media(media=types.InputMediaPhoto(
            media=image_logo, 
            caption="Ваша ссылка для подключения нового пользователя:\n\n"
                    f"*{link}*\n\n"
                    "Просто передай её томуу с кем хочешь вести совместный бюджет.",
            parse_mode="Markdown"),
            reply_markup=back_setting()
        )
    else:
        await callback.message.edit_media(media=types.InputMediaPhoto(
            media=image_logo, 
            caption="Вы уже подключены к другому пользователю"),
            reply_markup=back_setting()
        )