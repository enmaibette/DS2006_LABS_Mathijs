from dice import *

rounds = 0
winning_score = 3
player_names = []
player_wins = []
gameover = False

number_of_players = int(input("Enter number of players: "))

for i in range(number_of_players):
    name = input(f"Enter name for player {i+1}: ")
    player_names.append(name)

for i in range(number_of_players):
    player_wins.append(0)

player_roll__history = []

for i in range(number_of_players):
    player_roll__history.append([])

while gameover is False:
    print(f"Round {rounds+1}:")

    current_rolls = []

    for i in range(number_of_players):
        roll1 = rollD6()
        roll2 = rollD6()
        roll = roll1 + roll2
        current_rolls.append(roll)
        player_roll__history[i].append(roll)
        print(f"{player_names[i]} rolled a {roll}")

    input("Press Enter to continue...")

    max_roll = max(current_rolls)

    winners = []

    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    
    print(f"Winners of this round are: {winners}")

    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            gameover = True
            print(f"\n {player_names[z]} is the newest Battle of Dices World Champion!")

    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

    rounds += 1

filename = input("Enter a filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = " "
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_roll__history[i][round_number]} ")
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"Saving {rolls_str}")

        file.write(rolls_str + "\n")
