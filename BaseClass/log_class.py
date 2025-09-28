import logging

class LogCLassAll:
    def __init__(self):
        # --- основной logger бота ---
        self.logger = logging.getLogger("BotLogger")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            self.fh = logging.FileHandler("log/bot_new.log", 'w', encoding="utf-8")
            self.fh.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )
            self.fh.setFormatter(formatter)

            self.logger.addHandler(self.fh)
            
        # --- logger aiogram ---
        aiogram_logger = logging.getLogger("aiogram")
        aiogram_logger.setLevel(logging.DEBUG)

        if not aiogram_logger.handlers:
            fh_aiogram = logging.FileHandler("log/aiogram.log", 'w', encoding="utf-8")
            fh_aiogram.setLevel(logging.DEBUG)

            formatter_aiogram = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )
            fh_aiogram.setFormatter(formatter_aiogram)

            aiogram_logger.addHandler(fh_aiogram)

        # --- logger SQLAlchemy ---
        sa_logger = logging.getLogger("sqlalchemy.engine")
        sa_logger.setLevel(logging.INFO) 
        if not sa_logger.handlers:
            fh_sa = logging.FileHandler("log/sqlalchemy.log", 'w', encoding="utf-8")
            fh_sa.setLevel(logging.INFO)
            formatter_sa = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )
            fh_sa.setFormatter(formatter_sa)
            sa_logger.addHandler(fh_sa)
        
    def warning(self, text: str):
        print(text)
        self.logger.warning(text)
        
    def error(self, text: str):
        print(text)
        self.logger.error(text)
        
    def info(self, text: str):
        print(text)
        self.logger.info(text)
        
    def debug(self, text: str):
        print(text)
        self.logger.debug(text)
