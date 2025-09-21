from pathlib import Path
import base64
from aiogram.types import FSInputFile  # <--- важно
from dotenv import load_dotenv
import os

load_dotenv()

LINK_BOT = os.getenv("LINK_BOT")

class Images:
    _base_path = Path("images")
    _cache = {}

    @classmethod
    def get(cls, filename: str) -> FSInputFile:
        if filename not in cls._cache:
            path = cls._base_path / filename
            cls._cache[filename] = FSInputFile(path=str(path))  # корректный способ
        return cls._cache[filename]

    @classmethod
    def welcome_image(cls) -> FSInputFile:
        return cls.get("welcome.png")

    @classmethod
    def logo(cls) -> FSInputFile:
        return cls.get("logo.png")
    
    @classmethod
    def add_category(cls) -> FSInputFile:
        return cls.get("add_category.png")
    
    @classmethod
    def add_spending(cls) -> FSInputFile:
        return cls.get("add_spending.png")

    @classmethod
    def setting(cls) -> FSInputFile:
        return cls.get("setting.png")

class Read:
    def read_txt(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            token = file.read()
        return token
    
    def search_symbol(category: str):
        if '_' in category:
            return True
        else:
            return False

    async def checking_number(value):
        try:
            if ',' in value:
                return False

            if any(ch.isalpha() for ch in value):
                return False

            float(value)
            return True

        except ValueError:
            return False
        
class Text:
    welcome_text = Read.read_txt('text/welcome.txt')
    
class Generate:
    async def generate_link(user_id: int) -> str:
        payload = base64.urlsafe_b64encode(str(user_id).encode()).decode()
        return f"https://t.me/{LINK_BOT}?start=share_{payload}"
    
    async def encode_user_id(payload: str) -> int:
        padding = "=" * (-len(payload) % 4)

        decoded = base64.urlsafe_b64decode(payload + padding).decode()
        return int(decoded)