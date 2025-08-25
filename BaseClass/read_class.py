
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
            value_str = str(value).lstrip('-').replace('.', '', 1)
            return value_str.isdigit()
        except all:
            return False