import os

def read(path):
    with open(path, 'r', encoding='utf-8') as file:
        token = file.read()
        return token

def read_file():
    if os.uname().nodename == "PK":
        path_to_token = '/home/egor/token/test.txt'
        token = read(path_to_token)
    else:
        path_to_token = '/home/token/home_token.txt'
        token = read(path_to_token)[-1]
    return token

