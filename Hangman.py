# Creating the hangman game in Python
# Need to start by importing a random word which the user will ahve to guess
# There will be 7 lives if lives reaches 0 the user loses
# If the user guesses the word before their lives expire they win

# Need a pointer to iterate over the word if the user guess equals a letter print it
# Contain the game logic in a while loop controlled by the number of lives
# Create multiple functions
# One for the explanation of the game
# One for displaying the printed letters
# One for the game logic
# One for the statement if the player wins or loses
import random

word_list = ["ardvark", "baboon", "camel"]  # works
wordSelection = random.choice(word_list)
wordSelection1 = [i for i in wordSelection]


def intro():  # works
    print("Welcome to Hangman!")
    print("You have 7 chances to guess the correct word")
    print("If you guess a letter that is contained in the word you keep your lives")
    print("If you guess a letter that is not in the word you lose a life")
    print("If you guess the incorrect word you lose a life")
    print("Guess the word before you run out of lives")


# def word_update():
#     pass


def game_logic():
    lives = 7
    string = ["_" for i in range(len(wordSelection))]
    while lives > 0:
        guess = input("input a letter or guess the word")
        if guess == wordSelection:
            print(
                f"Congratulations! you correctly guessed the word {wordSelection}")
        for i in range(len(wordSelection)):
            if guess == wordSelection[i]:
                string.pop(i)
                string.append(guess[i])
                print(string)
            else:
                lives -= 1


intro()
game_logic()
