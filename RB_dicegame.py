"""
Rahul Boaz
Intensive Data Science II
Ms. Pan
Dice Game Project
In this game, the player's objective is to move the bus down the road.
The expected value of the dice roll is: -1.67
Sources used:
- https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
- https://stackoverflow.com/questions/23623288/print-full-ascii-art
- https://stackoverflow.com/questions/5254445/how-to-add-a-string-in-a-certain-position
- https://www.asciiart.eu/vehicles/busses
- https://www.geeksforgeeks.org/ternary-operator-in-python/
"""
import random
from time import sleep

# Modified ASCII Bus art
bus = [
    "  __[]__",
    " |  Bus |",
    " -o----o-"
]

def print_slow(text):
    """A function that prints one character at a time."""
    for x in text:                    # Cycle through the text
        print(x, end='', flush=True)  # Print character, no new line
        sleep(0.02)                   # Delay between characters
    print()                           # New line
    sleep(0.3)                        # Delay after finishing the line

# Bus position displayer
def display_bus(position, road_length=100):
    for line in bus:
        print(" " * position + line)
    print("_" * road_length)

score = 100
bus_position = score // 5
road_length = 100

# Welcome text
print_slow("Welcome to Rahul's Bus Dice Game!")
print_slow("Your goal is to move your bus as far as possible along the road.")
print_slow("The bus moves 1 place for every 5 points!")
print_slow("If you roll a 1, you win the bet!")
print_slow("If you roll a 3, 4, 5, or a 6 you lose the bet!")
print_slow("If you roll a 2, you have a random chance to win 1x, 2x, or 3x the bet!!")
display_bus(int(bus_position))

while score > 0:
    dice_roll = random.randint(1, 6)

    # Betting
    while True:
        bet = input(f"Enter # of points to bet or type 'quit' to quit. (Max: {score}): ")
        if bet == "quit":
            break
        try:
            val = int(bet)
            if val > 0 and val <= score:
                break
            else:
                print_slow(f"Invalid bet. Please enter a positive whole number between 1 and {score}.")
        except ValueError:
            print_slow("That's not a whole number!")
    if bet == "quit":
        break
    bet = int(bet)

    # Dice roll validation
    if dice_roll == 2:
        print_slow(f"You rolled a 2!")
        x = random.randint(1,3)
        score +=  x * bet
        print_slow(f"You won {x * bet} points!")
        bus_position = score // 5 if score > 0 else 0
        display_bus(int(bus_position), road_length)


    elif dice_roll == 1:
        print_slow(f"You rolled a {dice_roll}. You move forward!")
        score += bet
        bus_position = score // 5
        display_bus(int(bus_position), road_length)

    elif dice_roll == 3 or dice_roll == 5 or dice_roll == 6 or dice_roll == 4:
        print_slow(f"Sorry, you rolled a {dice_roll}. You lose {bet} points.")
        score -= bet
        bus_position = score // 5 if score > 0 else 0
        display_bus(int(bus_position), road_length)


    if score <= 0:
        break

    # # Quit yes/no
    # while True:
    #     play = input("Would you like to keep playing? (yes/no): ").lower()
    #     if play == "yes":
    #         print_slow("Game continues!")
    #         break
    #     elif play == "no":
    #         print_slow("Thank you for playing!")
    #         break
    #     else:
    #         print_slow("Invalid input. Please enter yes or no.")
    #
    # if play == "no":
    #     break

# End of Game
if score > 0:
    print_slow(f"Congratulations! You finished with {score} points!")
    print_slow(f"The bus moved all the way to position {bus_position}!")
else:
    print_slow("GAME OVER. You lost everything.")
print_slow("Thank you for playing!")