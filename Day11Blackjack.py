import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = random.choices(cards, k=2)
dealers_cards = random.choices(cards, k=2)


def comp_draw():
    dealers_cards.append(random.choice(cards))  # write the code for computer keep playing?
    return dealers_cards


def user_draw():
    user_cards.append(random.choice(cards))
    return user_cards


# def play_game():
is_repeat = True
while is_repeat:
    print(f"Your cards: {user_cards}")
    print(f"Computer's card: {dealers_cards}")
    print(f"Computer's first card: {dealers_cards[0]}")

    sum_user = sum(user_cards)
    print(f"Your current score: {sum_user}")

    sum_comp = sum(dealers_cards)
    print(f"Computer score: {sum_comp}")

    blackjack = 11 + 10
    if (sum_user == 21 and len(user_cards) == 2):
        sum_user = blackjack
    if (sum_comp == 21 and len(dealers_cards) == 2):
        sum_comp = blackjack

    if sum_user == blackjack:
        if sum_comp != blackjack:
            result = "Win"
            break
    elif sum_comp == blackjack:
        result = "Lose"
        break
    elif sum_user > 21:
        if 11 not in user_cards:
            result = "Lose"
            break
        else:
            x = user_cards.index(11)  # index of 11
            user_cards[x] = 1  # change 11 to 1
            sum_user = 0
            for i in user_cards:
                sum_user += i
            print(f"Your current score: {sum_user}")
            if sum_user > 21:
                result = "Lose"
                break
            else:
                draw = input("Type 'y' to draw another card, type 'n' to pass: \n")
                if draw == 'y':
                    user_draw()     # user to draw another card
                elif draw == 'n':
                    if sum_comp < 17:
                        comp_draw()
                    elif sum_comp > 21:
                        result = "Win"
                        break
                    elif sum_user > sum_comp:
                        result = "Win"
                        break
                    elif sum_user < sum_comp:
                        result = "Lose"
                        break
                    elif sum_user == sum_comp:
                        result = "Draw"
                        break
                    else:
                        is_repeat = False
    else:
        draw = input("Type 'y' to draw another card, type 'n' to pass: \n")
        if draw == 'y':
            user_draw()  # user to draw another card
        elif draw == 'n':
            if sum_comp < 17:
                comp_draw()
            elif sum_comp > 21:
                result = "Win"
                break
            elif sum_user > sum_comp:
                result = "Win"
                break
            elif sum_user < sum_comp:
                result = "Lose"
                break
            elif sum_user == sum_comp:
                result = "Draw"
                break
            else:
                is_repeat = False

print(f"Your final hand: {user_cards}, final score: {sum_user}.")
print(f"Computer final hand: {dealers_cards}, final score: {sum_comp}.")
print(f"You {result}")


# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
# play_game()