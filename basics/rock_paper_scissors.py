###################################################
# Rock, paper, scissors
###################################################

# Rock paper scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign (also indicating "victory" or "peace") except that it is pointed horizontally instead of being held upright in the air. A simultaneous, zero-sum game, it has only two possible outcomes: a draw, or a win for one player and a loss for the other.
# A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie.

# Rock paper scissors is often used as a fair choosing method between two people, similar to coin flipping, drawing straws, or throwing dice in order to settle a dispute or make an unbiased group decision.
# https://en.wikipedia.org/wiki/Rock_paper_scissors

# Concepts Illustrated
# * Python variables
# * list data structure
# * control structures
# * while loop
# * break statement
# * random selection


# import random module
from random import randint
# Create a list of play options
play_options = ["rock", "paper", "scissors"]

# Initialize a variable to store player's game choice (rock, paper, or scissors)
player = ""

# Keep playing the game until the player enters "quit"
while player != 'quit':
    
    # Get input from the player
    player = input("Please enter 'rock', 'paper', 'scissors' to play, or 'quit' to stop: ")
    
    # Assign a random play to the computer and select a corresponding value from the play_options list
    computer = play_options[randint(0,2)]
    
    
    if player == computer: # Both player and computer chose the same value
        print("Tie!")
    elif player == "rock": # Player chose "rock"
        if computer == "paper": # Computer randomly selected "paper"
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper": # Player chose "paper"
        if computer == "scissors": # Computer randomly selected "scissors"
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors": # Player selected "scissors"
        if computer == "rock": 
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "quit":
        break
    else:
        print("That's not a valid play. Check your spelling!")
    