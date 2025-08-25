def checking_number(value):
    value_str = str(value).lstrip('-').replace('.', '', 1)
    return value_str.isdigit()

print(checking_number(10,3))