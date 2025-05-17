import datetime

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from aiogram import Bot
from aiogram.types import BufferedInputFile
import sqlite3


def format_amount(amount):
    try:
        num = int(amount)
        return "{:,}".format(num).replace(",", " ")
    except:
        return str(amount)

async def create_table_image(bot: Bot, i):
    try:
        # 1. Получаем данные из БД
        with sqlite3.connect('db/home.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT category, sum_money FROM plan")
            rows = cursor.fetchall()

        # 2. Создаем изображение таблицы
        img_width = 400
        img_height = 350
        img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        # 3. Устанавливаем шрифты
        try:
            title_font = ImageFont.truetype("arial.ttf", 20)  # Шрифт для заголовка
            font = ImageFont.truetype("arial.ttf", 14)  # Шрифт для таблицы
        except:
            title_font = ImageFont.load_default()
            font = ImageFont.load_default()

        # 4. Добавляем заголовок с текущим месяцем и годом
        current_month = datetime.datetime.now().strftime("%B %Y")  # Например: "May 2025"
        title = f"Финансовый отчет за {current_month}"

        # Центрируем заголовок
        title_width = draw.textlength(title, font=title_font)
        draw.text(
            ((img_width - title_width) / 2, 20),
            title,
            font=title_font,
            fill=(0, 0, 0)  # Черный цвет текста
        )

        # 3. Рисуем заголовки
        headers = ["Категория", "Сумма (руб)"]
        x_positions = [50, 250]  # Позиции колонок

        y = 80  # Начинаем таблицу ниже заголовка
        for i, header in enumerate(headers):
            draw.text((x_positions[i], y), header, font=font, fill=(0, 0, 128))  # Темно-синий цвет

        # 4. Рисуем данные
        y += 30
        sum_money = 0
        for row in rows:
            for i, cell in enumerate(row):
                text = format_amount(cell) if i == 1 else str(cell)
                draw.text((x_positions[i], y), text, font=font, fill=(0, 0, 0))
                is_number = lambda value: True if str(value).lstrip('-').replace('.', '', 1).isdigit() else False
                if is_number(cell):
                    sum_money += cell
            y += 25

        # 5. Сохраняем изображение в буфер
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')  # Важно: save вызывается у img!
        img_byte_arr.seek(0)

        await bot.send_photo(
            chat_id=i,
            photo=BufferedInputFile(
                img_byte_arr.getvalue(),
                filename="categories_report.png"
            ),
            caption=f"Осьалось: {sum_money}"
        )

    except Exception as e:
        error_msg = f"Ошибка при создании отчета: {str(e)}"
        print(error_msg)
