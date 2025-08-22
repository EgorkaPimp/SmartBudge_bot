from aiogram import Dispatcher, Router, Bot
from BaseClass.log_class import LogCLassAll
from token_file import read_file

class Router:
    my_router = Router()

class StartBot:
    def __init__(self):
        self.dp = Dispatcher()
        self.dp.include_router(Router.my_router)
        LogCLassAll().info("Start bot")

    async def run(self):
        await self.dp.start_polling(InstanceBot.bot)
    
class InstanceBot:
    my_token = read_file()
    bot = Bot(token=my_token)