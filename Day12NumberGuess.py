import random

print("Welcome to the number guessing game. \nI'm thinking of a number between 1 and 100. \n")


def compare(comp_num, guess):
    if guess == comp_num:
        return f"You got it right! The answer was {comp_num}."
    elif guess < comp_num:
        return "Too low."
    elif guess > comp_num:
        return "Too high."


comp_num = random.randint(1, 100)
# print(comp_num)
user_chose = input("Chose a difficulty. Type 'easy' or 'hard': ")

if user_chose == 'easy':
    attempts = 10
elif user_chose == 'hard':
    attempts = 5

# is_pay = True
while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    result = compare(comp_num, guess)
    if result == "Too low.":
        print("Too low.")
        attempts = attempts - 1
    elif result == "Too high.":
        print("Too high.")
        attempts = attempts - 1
    elif result == f"You got it right! The answer was {comp_num}.":
        print(f"You got it right! The answer was {comp_num}.")
        attempts = 0
    if attempts == 0:
        print("Game ends.")
    elif guess != comp_num:
        print("Guess again!")