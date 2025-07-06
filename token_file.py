def read_file():
    with open('/home/egor/token/home_bot.txt', 'r', encoding='utf-8') as file:
        token = file.read()
    return token