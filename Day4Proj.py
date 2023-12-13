import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user_input = int(input())  # 0 for Rock, 1 for Paper or 2 for Scissors.
if user_input == 0:
    print(f"You chose: \n Rock {rock}")
elif user_input == 1:
    print(f"You chose: \n Paper {paper}")
elif user_input == 2:
    print(f"You chose: \n Scissors {scissors}")
else:
    exit("Incorrect input")

comp_chose = random.randint(0, 2)
if comp_chose == 0:
    print(f"Computer chose: \n Rock {rock}")
elif comp_chose == 1:
    print(f"Computer chose: \n Paper {paper}")
elif comp_chose == 2:
    print(f"Computer chose: \n Scissors {scissors}")

# Rock cuts Scissors, Scissors cut Paper, Paper cuts Rock

if user_input == 0:
    if comp_chose == 0:
        print("You tie.")
    elif comp_chose == 1:
        print("You lose.")
    elif comp_chose == 2:
        print("You win.")
elif user_input == 1:
    if comp_chose == 0:
        print("You win.")
    elif comp_chose == 1:
        print("You tie.")
    elif comp_chose == 2:
        print("You lose.")
elif user_input == 2:
    if comp_chose == 0:
        print("You lose.")
    elif comp_chose == 1:
        print("You win.")
    elif comp_chose == 2:
        print("You tie.")
