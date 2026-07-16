import random
import string

def generator():
    print()
    char_values = string.ascii_letters + string.digits + string.punctuation
    length = int(input("Length of the password: "))

    n = 1
    while n < 4:
        print(f"{n}.", end=" ")

        for _ in range(0,length):
            print(random.choice(char_values), end= "")

        print()
        n += 1

def indicator():
    print()
    password = input("Enter Password: ")

    char_len = "At least 8 characters long"
    upper_char = "Contains at least one uppercase letter"
    lower_char = "Contains at least one lowercase letter"
    num = "Contains at least one number"
    punc = "Contains at least one special character"
    
    count = 0
    U_status, L_status, num_satus, punc_status = False, False, False, False

    for i in password:
        if i in string.ascii_uppercase:
            U_status = True

        if i in string.ascii_lowercase:
            L_status = True
        
        if i in string.digits:
            num_satus = True
        
        if i in string.punctuation:
            punc_status = True

    if len(password) >= 8:
        print(char_len, "✅")
        count += 1
    else:
        print(char_len, "❌")
    
    if U_status:
        print(upper_char, "✅")
        count += 1
    else:
        print(upper_char, "❌")

    if L_status:
        print(lower_char, "✅")
        count += 1
    else:
        print(lower_char, "❌")

    if num_satus:
        print(num, "✅")
        count += 1
    else:
        print(num, "❌")
    
    if punc_status:
        print(punc, "✅")
        count += 1
    else:
        print(punc, "❌")
    
    score(count)

def score(score):
    if score <= 2:
        print("~ Weak Password 🔴~ ")
    elif score == 3:
        print("~ Medium Password 🟠~")
    elif score == 4:
        print("~ Strong Password 🟡~")
    else:
        print("~ Very Strong Password 🟢~")

while True:
    print("1 Password Generator")
    print("2 Password Indicator")
    print("0 Quit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            generator()
            print()
            continue
        if choice == 2:
            indicator()
            print()
            continue
        if choice == 0:
            break
        else:
            print("~INVALID INPUT~")
            print()
    except ValueError:
        print("~INVALID INPUT~")
        print()