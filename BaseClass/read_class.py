
class Read:
    def read_txt(path):
        with open(path, 'r', encoding='utf-8') as file:
            token = file.read()
        return token

    