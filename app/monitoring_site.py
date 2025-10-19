from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from aiogram.utils.markdown import hlink
from BaseClass.read_class import Images
from app.inline_back import back_menu

image_logo = Images.logo()

@RouterStore.my_router.callback_query(CallbackDataFilter("site_monitoring"))
async def site_monitoring(callback: types.CallbackQuery):
    LogCLassAll().debug("Press button: site_monitoring")
    user_id = callback.from_user.id
    link = f"http://monitorbot.duckdns.org/budget/{user_id}"
    message_text = (
    f"📊 <b>Твой личный дашборд расходов</b>\n\n"
    f"Следи за своими тратами и планами в удобной визуальной форме.\n"
    f"👉 {hlink('Открыть дашборд', link)}"
)
    await callback.message.edit_media(media=types.InputMediaPhoto(
            media=image_logo,
            caption=message_text,
            parse_mode="HTML"),
            reply_markup=back_menu())