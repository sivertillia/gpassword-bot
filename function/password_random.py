import random
from sqlighter import SQLighter

db = SQLighter('db/database.db')
list_password = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789', '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\'']

async def elem_password(result):
    password = ''
    list_password_i = 0
    for i in range(2, 6):
        if result[i] == 1:
            password = password + list_password[list_password_i]
        list_password_i += 1
    return password

async def generate_password(user_id, length=8):
    random_symbol = []
    results = db.user_settings(user_id)
    for result in results:
        elem = await elem_password(result)
        for i in range(int(length)):
            random_symbol.append(random.choice(elem))
        password = ''.join(random_symbol)
        return password

def int_in_str(what):
    if what >= 1:
        return 'On'
    elif what <=0:
        return 'Off'
    else:
        return 'Error'

def str_in_int(what):
    if what == 'on':
        return 1
    elif what =='off':
        return 0
    else:
        return 1