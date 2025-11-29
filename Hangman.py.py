import random


word = ["ram", "shyam", "raj", "aman", "hanuman"]

word = random.choice(word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.\n")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word+= letter
        else:
            display_word += "_"

    print("Word:", display_word)

    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter:"). lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
    else:
        print("Good guess!")

        print()

    if attempts == 0:
        print("You lost! The correct word was:", word)                   