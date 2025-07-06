import sqlite3
from io import BytesIO

from aiogram import Bot
from image_table import create_table_image
from aiogram.types import BufferedInputFile

base_categories = {'ремонт':40000,
                    'кредит':40000,
                    'комуналка':10000,
                    'проезд':10000,
                    'питание':25000,
                    'рестораны':16000,
                    'доставка':6000,
                    'здоровье':15000,
                    'бьюти хуюти':10000,
                    'личные Камила':14000,
                    'личные Егор':14000,
                   }

id = [933194755, 875300228]

def init_db():
    with sqlite3.connect('db/home.db') as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS plan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT UNIQUE,
                sum_money INTEGER 
            )
        ''')
        conn.commit()

        cursor.execute('''
                  CREATE TABLE IF NOT EXISTS expenses (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      category TEXT UNIQUE,
                      sum_money INTEGER 
                      month INTEGER
                  )
              ''')
        conn.commit()
    if search_base_db():
        print('db correct')
    else:
        base_category_and_data()


def base_category_and_data():
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        for category in base_categories:
            cursor.execute("INSERT INTO plan (category, sum_money)"
                           "VALUES (?, ?)",
                           (category, base_categories[category]))
            conn.commit()
    print('base cat created')

def search_base_db():
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM plan "
                       "WHERE category = ?",
                       ('еда',))
        return cursor.fetchone() is not None


async def base_category_update(bot: Bot = None):
    for i in id:
        await create_table_image(bot, i)
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        for category in base_categories:
            cursor.execute(
                "UPDATE plan SET sum_money = ? WHERE category = ?",
                (base_categories[category], category)
            )
        conn.commit()

async def reminder_day(bot: Bot):
    for i in id:
        await bot.send_message(
            chat_id=i,
            text='Я просто решил напомнить о себе'
        )


