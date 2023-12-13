import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
lives = 6   # Set 'lives' to equal 6.
# print(chosen_word)
# Check display
display = []
for letter in chosen_word:
    display += '_'
print(display)

while '_' in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"{guess} is already guessed.")
    for i in range(len(chosen_word)):  # Check guessed letter
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    print(display)
    if guess not in chosen_word:
        lives = lives - 1
        print(f"{guess} is not present in chosen word. You lose a life.")
    print(f"{lives} lives")
    print(hangman_art.stages[lives])
    if lives == 0:
        print("You lose.")
        break

    if '_' not in display:
        print(f"{''.join(display)}")
        print("You win.")



