from pathlib import Path
from aiogram.types import FSInputFile  # <--- важно

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
        return cls.get("welcome.jpg")

    @classmethod
    def logo(cls) -> FSInputFile:
        return cls.get("logo.png")

    @classmethod
    def banner(cls) -> FSInputFile:
        return cls.get("banner.jpg")

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