import random
import string

def gen_random_nick(length):
    characters = string.ascii_letters + string.digits
    nickname = ''.join(random.choice(characters) for _ in range(length))
    return nickname

try:
    nickname_length = int(input("Nickname uzunluğunu giriniz: ")) 
    random_nickname = gen_random_nick(nickname_length)
    print(random_nickname)
except ValueError:
    print("Geçersiz giriş. Lütfen bir tamsayı girin.")
