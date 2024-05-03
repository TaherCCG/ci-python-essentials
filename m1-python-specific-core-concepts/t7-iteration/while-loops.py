# While Loops in Python
"""
With the while loop we can execute a set of statements as long as a condition is true.
"""



# Runnable Example 1
print("Runnable Example 1: ")
print("Initiating Countdown Sequence...")
print("Lift Off Will Commence In...")

for countdown_number in range(10, -1, -1):
    print(f"{countdown_number} seconds...")
print("And We Have Lift Off!")

"""The above example demonstrates a countdown sequence that starts at 10 and counts down to 0
The while loop will continue to run as long as the condition is true
The condition is checked at the beginning of each iteration"""


# Runnable Example 2
print("Runnable Example 2: ")

play_game = True

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n ")

    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")

"""The above example demonstrates a simple game loop that will continue to run as long as the play_game variable is True
The user is prompted to input whether they would like to continue playing the game
If the user inputs 'y' the game will continue
If the user inputs 'n' the game will close
If the user inputs anything else they will be prompted to try again
The play_game variable is set to False when the user inputs 'n' which will end the loop
The while loop will continue to run as long as the condition is true
The condition is checked at the beginning of each iteration"""


