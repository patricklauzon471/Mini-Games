import random


def Introduction():
    print("Welcome to Rock Paper Scissors, Here are the rules:")
    print("On the count of three select either rock, paper, or scissors")
    print("paper beats rock")
    print("scissors beats paper")
    print("rock beats scissors")


#global variables
winner = None
computer = None
player = None
rock = 1
paper = 2
scissors = 3

Introduction()


def rules():
    if player_choice == 1 and computer_choice == 1:
        game = "tie"
    elif player_choice == 2 and computer_choice == 2:
        game = "tie"
    elif player_choice == 3 and computer_choice == 3:
        game = "tie"
    elif player_choice == 1 and computer_choice == 2:
        winner = computer
    elif player_choice == 1 and computer_choice == 3:
        winner = player
    elif player_choice == 2 and computer_choice == 1:
        winner = player
    elif player_choice == 2 and computer_hoice == 3:
        winner = computer
    elif player_choice == 3 and computer_choice == 1:
        winner = computer
    elif player_choice == 3 and computer_choice == 2:
        winner = player


def games():
    global rules
    player_choice = input(
        "Select 1 for rock, 2 for paper, and 3 for scissors: \n")
    if player_choice in range(1, 3):
        print("you have selected {0}".format(player_choice))
    computer_choice = random.randint(1, 3)
    if player_choice == computer_choice:
        print(game)
    elif winner == computer:
        print("The computer is the winner")
    elif winner == player:
        print("You win!")


games()
