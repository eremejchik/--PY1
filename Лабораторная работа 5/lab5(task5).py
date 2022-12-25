import random
import string

def get_random_password(n = 8) -> str: #задали длину пароля
    new_list = string.ascii_letters + string.digits
    changed_list = "".join(random.sample(new_list, 8)) # TODO написать функцию генерации случайных паролей
    return changed_list
print(get_random_password())
