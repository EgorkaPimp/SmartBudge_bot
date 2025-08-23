import os
from BaseClass.read_class import Read

def read_file():
    if os.uname().nodename == "PK":
        path_to_token = '/home/egor/token/test.txt'
        token = Read.read_txt(path_to_token)
    else:
        path_to_token = '/home/token/home_token.txt'
        token = Read.read_txt(path_to_token)[:-1]
    return token