from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types
from app.inline_button import app_menu
from app.inline_back import back_menu
from BaseClass.read_class import Images
from db_postgres.crud.wishes import add_wish

image_logo = Images.add_category()

class Add_Finance(StatesGroup):
    waiting_wish = State()
    
@RouterStore.my_router.callback_query(CallbackDataFilter("suggest_feature"))
async def suggest_feature(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug("Press button: suggest_feature")
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("💡 У вас есть идея? \n"
                                  "Напишите своё предложение по улучшению проекта — любая мысль поможет сделать его лучше!",
                                  reply_markup=back_menu())
    await state.set_state(Add_Finance.waiting_wish)
    
@RouterStore.my_router.message(Add_Finance.waiting_wish)
async def add_comment(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    comment = message.text
    
    await add_wish(user_id=user_id,
                   comment=comment)
    
    await message.answer_photo(photo=image_logo,
                        caption='*✨ Ваши идеи важны!*\n'
                        'Большое спасибо что приняли участие',
                        parse_mode='Markdown',
                        reply_markup=app_menu())
    