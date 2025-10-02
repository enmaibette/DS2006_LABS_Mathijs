from dice import *
import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round = 0

while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")

    player1_roll = rollD6() 
    player2_roll = rollD6()

    # Players roll dice
    print("Player 1 rolled: ", player1_roll)
    print("Player 2 rolled: ", player2_roll)


    # Determine round winner
    if player1_roll > player2_roll:
        player1_wins += 1
        round += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player1_roll == player2_roll:
        round +=1 
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins += 1
        round += 1 
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)

    # Show current game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# When loops ends, someone reached 3 wins
if player1_wins == 3:
    print("PLAYER 1, YOU ARE THE WOLRD CHAMPION!")
    print("It took you ", round, " rounds to win the game.")
else:
    print("PLAYER 2, YOU ARE THE WOLRD CHAMPION!")
    print("It took you ", round, " rounds to win the game.")

