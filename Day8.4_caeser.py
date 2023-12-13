from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount = shift_amount * -1
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += i   # start_text[start_text.index(i)]
    print(f"The {direction}d message is {end_text}")


repeat = 'yes'
while repeat == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))     # shift = shift % 26 -- another way of declaring large shift
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if repeat == 'no':
        print("Goodbye")



# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for i in text:
#         index1 = alphabet.index(i)
#         index2 = (index1+shift)%26
#         cipher_text = cipher_text + alphabet[index2]
#     print(f"The encoded message is {cipher_text}")
#     return cipher_text
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for i in cipher_text:
#         position = alphabet.index(i)
#         new_position = (position-shift_amount)%26
#         plain_text = plain_text + alphabet[new_position]
#     print(f"the decoded message is {plain_text}")


# encrypt(plain_text=text, shift_amount=shift)
#
# decrypt(cipher_text=text, shift_amount=shift)

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)