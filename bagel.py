# bagels project
# deductive logic game, you must guess a secret three-digit number based on clues.
# The game offers one of the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the wrong place,
# “Fermi” when your guess has a correct digit in the correct place, and
# “Bagels” if your guess has no correct digits.
# You have 10 tries to guess the secret number.


# Generate a 3 digit number
import random

# Convert the integer to a string
number = str(random.randint(100, 999))


# Game logic
def game():
    tries = 0
    for tries in range(0, 9):

        guess = input('Enter a 3 digit number ')

        if guess == number:
            break

        elif guess[0] == number[0]:
            print('Fermi')
        elif guess[0] == number[1]:
            print('Pico')
        elif guess[0] == number[2]:
            print('Pico')

        if guess[1] == number[0]:
            print('Pico')
        elif guess[1] == number[1]:
            print('Fermi')
        elif guess[1] == number[2]:
            print('Pico')

        if guess[2] == number[0]:
            print('Pico')
        elif guess[2] == number[1]:
            print('Pico')
        elif guess[2] == number[2]:
            print('Fermi')

        else:
            print('Bagel')

        tries += 1

        print('Your guess is incorrect, the number of tries is', tries)

    if tries == 9:
        print('You lost')
    else:
        print('You won')


game()
