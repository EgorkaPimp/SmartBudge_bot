def read_file():
    with open('/home/token/home_token.txt', 'r', encoding='utf-8') as file:
        token = file.read()
    return token
