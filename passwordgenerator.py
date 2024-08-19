import random
import sys
import string
length = int(input("Enter the length of the password: "))
if length==0:
    print("Enter a valid number for the password length.")
    sys.exit()

letters = input("Do you want to include letters? (y/n): ").upper() == 'Y'
num = input("Do you want to inlude numbers? (y/n): ").upper() == 'Y'
sym = input("Do you want to include symbols? (y/n): ").upper() == 'Y'

def generate_password(length,letters=True, num=True,sym=True):
    char = ""
    5
    if letters:
        char += string.ascii_letters
    if num:
        char += string.digits
    if sym:
        char += string.punctuation

    password = ''.join(random.choice(char) for i in range(length))
    return password

password = generate_password(length,letters,num,sym)
print("Your generated password is:", password)

