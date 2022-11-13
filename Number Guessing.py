# Number guessing game between 1 and 100
# Create an easy mode and hard mode
# For easy mode the user has 10 guesses
# For the hard mode the user has 5 guesses
# Tell the user after every guess whether their guess is higher or lower than the number

import random

# Generate random number
number = random.randint(1, 100)
turns = 0
# Return the number of lives a player has based on their input

# Create a fucntion to retrive the number of lives you have remaining


def modes():
    mode = input(" Type 'e' for easy mode and 'h' for hard mode: ")
    if mode == "e":
        return 10
    elif mode == "h":
        return 5
    else:
        print("This is an invalid input please try again")


turns = modes()

while turns > 0:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Guess is too low")
    elif guess > number:
        print("Guess is too high")
    elif guess == number:
        print(f"You guessed it! the correct numnber is {number}")
    turns -= 1
