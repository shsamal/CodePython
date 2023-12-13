# secret bidding
# import os
from art1 import logo
print(logo)

dict_bid = {}
is_bid = True

while is_bid == True:
    name = input("What is your name? \n")
    bid = float(input("What is your bid price? $ \n"))
    dict_bid.update({name: bid})
    # add_new_bid(name, bid)
    any_bid = input("Are there any other bidders? type 'yes' or 'no'. \n").lower()
    if any_bid == 'yes':
        is_bid = True
        # os.system('cls')
    elif any_bid == 'no':
        is_bid = False

print(dict_bid)
value = 0
winner = ""
for i in dict_bid:
    bid_amount = dict_bid[i]
    if bid_amount > value:
        value = bid_amount
        winner = i

print(f"The winner of the bid is {winner} with bid value: $ {value}.")

#     if dict_bid[i] > value:
#         value = dict_bid[i]
#     else:
#         value = value
#
# winner = ""
# for key in dict_bid:
#     if dict_bid[key] == value:
#         winner = key











