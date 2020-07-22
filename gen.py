import random
import string

LETTERS = string.ascii_letters
NUMBERS = '0123456789'
SPECIAL = '+-*&^$@'
SYMBOLS = LETTERS + NUMBERS + SPECIAL 

length = int(input('enter password length:'))
password = ''.join(random.sample(SYMBOLS, length))
print(password)