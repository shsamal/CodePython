# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# l1 = "" or [] : str OR list
# for l in range(0, nr_letters):
#     l1 += (random.choice(letters)) for str OR l1.append(random.choice(letters)) for list
# print(l1)

l1 = random.sample(letters, nr_letters)
s1 = random.sample(symbols, nr_symbols)
n1 = random.sample(numbers, nr_numbers)
password = l1 + s1 + n1
print(password)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for p in password:
    print(p, end='')


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
print('\n', password)
ur_password = "" # changing list back to str
for p in password:
    ur_password += p
print(f"Your password is: {ur_password}")



