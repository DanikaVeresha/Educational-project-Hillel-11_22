import random


def user_password():
    chars = '#<>@$%^&*!abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = 30
    length = int(length)
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


result = user_password()
print(result)


