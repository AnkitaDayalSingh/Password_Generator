import random
import string

char_values = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(0,12):
    print(random.choice(char_values), end= "")
