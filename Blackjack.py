# Blackjack game
# Simplified version

# Given two randomized cards
# Computer given two randomized cards
# Have to get as close to 21 as possioble without going over
# Choose to get another card ort keep the cards you have
# Initially displays your cards and one of the computer's cards
# If you the user doesn't go over 21 and their card value is higher than the computer's they win
# If the user goes over 21 or the computer has the higher card value they lose

# Create a dictionary that matches the card to it's value

import random

# Need as list of card values that matches their value in the game, face cards all equal 10

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Assign two random cards to the user and the computer

# Function to return a random card from the list
def deal_card():
    # Indexes a random number based on the range of the list
    random_number = random.randint(0, len(cards)-1)
    card = cards[random_number]
    return card

# Function to sum the value of all the cards regardless of how many cards are in hand


def calculate_score(cards):
    # 0 indicates a blackjack as the sum of the cards is 21
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

# If the sum of the cards is greater than 21 can assume the user would select 1 instead of 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# User and computer cards are stored in an initially empty list
user_cards = []
computer_cards = []
# Need to set this condition for the while loop to initiate and eventually end
is_game_over = False

# For loop created to deal the user and computer two cards
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while not is_game_over:
    # Scores calculated by subbing in the user scores as a variable for the calculate score function
    # The function sums the scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Display the users hand to the user but only the first card for the computer
    # Can be altered so that no computer cards are shown to make it more challenging
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    # Game ends with either the user or computer gets a blackjack or the user has overdrawn
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    # If the game over condition isn't met the user has the chance to draw another card
    # If another card is drawn this process repeats or else the scores are compared
    else:
        user_should_deal = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

# Computer automated to draw a card when it's score is less than 17 as thbis follows
# a realistic decision a player would make
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


# User score and computer score are compared as they are passed in as variables
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has a blackjack, you lose"
    elif user_score == 0:
        return "You win, you have a blackjack"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


print(compare(user_score, computer_score))
