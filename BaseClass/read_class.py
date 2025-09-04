
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