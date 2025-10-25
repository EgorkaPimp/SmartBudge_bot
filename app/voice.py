from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types, F
from aiogram.fsm.context import FSMContext
import os
import re
import datetime
import speech_recognition as sr
from pydub import AudioSegment
from db_postgres.crud.expenses import get_expenses, add_to_expenses
from db_postgres.crud.shares import status_share_search
from db_postgres.crud.every_waste import add_record
from app.inline_button import add_voice, app_menu
from app.inline_back import back_menu
from BaseClass.read_class import Images

recognizer = sr.Recognizer()
image_logo = Images.add_spending()

@RouterStore.my_router.message(F.voice)
async def handle_voice(message: types.Message, state: FSMContext):
    LogCLassAll().debug('Send voice message')
    
    file = await message.bot.get_file(message.voice.file_id)
    
    ogg_path = "voice.ogg"
    wav_path = "voice.wav"
    await message.bot.download_file(file.file_path, ogg_path)

    sound = AudioSegment.from_file(ogg_path)
    sound.export(wav_path, format="wav")
    
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU,en-US")
            LogCLassAll().debug(f'Voice message: {text}')
            
            master = await status_share_search(message.from_user.id)
            if master:
                user_id = master.master_id
            else:
                user_id = message.from_user.id
            
            categories_db = await get_expenses(user_id=user_id)
            search_category = next(
                    (word for category in categories_db for word in text.split() 
                    if word.lower() == category.category.lower()), 
                    None)
            
            if search_category is None:
                await message.answer(f"🗣 Распознанный текст:\n{text}\n"
                                             "Не получилось определить категорию.")
                return
            
            numbers = re.findall(r"\d+", text)
            numbers = [int(n) for n in numbers] if numbers else [] 
            
            await message.answer(f"🗣 Распознанный текст:\n{text}\n"
                                 "───────────────\n"
                                 f"📦 Категория: ✨*{search_category.capitalize()}*\n" 
                                 f"💵 Сумма: {float(sum(numbers))}",
                                 parse_mode='Markdown',
                                 reply_markup=add_voice())
            
            await state.update_data(category=search_category)
            await state.update_data(spending=float(sum(numbers)))
            
        except sr.UnknownValueError:
            await message.answer("Не удалось распознать речь 😞",
                                 reply_markup=back_menu())
            return
        except sr.RequestError:
            await message.answer("Ошибка при подключении к сервису распознавания 😕",
                                 reply_markup=back_menu())
            return
        finally:
            os.remove(ogg_path)
            os.remove(wav_path)
    
@RouterStore.my_router.callback_query(CallbackDataFilter("yes_add"))
async def add_spending(callback: types.CallbackQuery, state: FSMContext):
    LogCLassAll().debug('Voice message add spending')
    await callback.answer()
    await callback.message.delete()
    
    data = await state.get_data()
    
    master = await status_share_search(callback.from_user.id)
    if master:
        user_id = master.master_id
    else:
        user_id = callback.from_user.id
        
    category = data['category']
    spending = data['spending']
    
    print(f"{category}      {spending}")
        
    new_db = await add_to_expenses(user_id=user_id,
                                    category=category,
                                    amount_to_add=spending)
    
    await add_record(user_id=user_id,
                    category=category,
                    expense=float(spending),
                    data=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    await callback.message.answer_photo(photo=image_logo,
                                    caption=f'💎 Готово! Новый остаток {new_db.amount_expenses} '
                                    f'уже в категории {category}. ✨',
                                    reply_markup=app_menu())
    await state.clear()
        
    
    
    