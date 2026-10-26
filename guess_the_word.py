# Hernan Villegas
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of words the game can choose from
words = ["apple", "banana", "orange", "grape", "peach"]


# Choose a random word
def choose_word():
    return random.choice(words)


# Check whether a guessed letter is in the word
def check_guess(word, letter):
    return letter in word


# Start the word guessing game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Guess the Word!")

    while attempts > 0:
        # Display correctly guessed letters
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"

        print("\nWord:", display)

        # Check whether the entire word has been guessed
        if "_" not in display:
            print("Congratulations! You guessed the word!")
            break

        print("Attempts remaining:", attempts)
        guess = input("Guess a letter: ").lower()

        # Make sure the player enters one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if check_guess(word, guess):
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

    if attempts == 0:
        print("Game over! The word was:", word)


# Run the game
if __name__ == "__main__":
    play_game()
