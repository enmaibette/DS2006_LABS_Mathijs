# import random

# # Input from the user to roll the dice
# while True:
#     key = input("Press Enter to roll the dice...")
#     if key == "":
#         break

# # Generate a random number between 1 and 20
# result = random.randint(1, 20)

# # Show the result
# print("You rolled a", result, "on a 20-sided dice.")

import random

def rollD4():
    return random.randint(1, 4)

def rollD6():
    return random.randint(1, 6)

def rollD8():
    return random.randint(1, 8)

def rollD10():
    return random.randint(1, 10)

def rollD12():
    return random.randint(1, 12)    

def rollD20():
    return random.randint(1, 20)

def rollD100(): 
    return random.randint(1, 100)
