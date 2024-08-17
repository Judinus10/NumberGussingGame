import random

# Generating a random number between 1 and 100
num = random.randint(1, 100)

# Asking the user to guess the number
guess = int(input("Guess a number between 1 to 100: "))

# Loop to allow the user 3 chances to guess
i = 0 

while i < 3:
    if num > guess:
        print("Your guess is too low!")
    elif num < guess:
        print("Your guess is too high!")
    else:
        break  # Exit the loop if the guess is correct
    
    i += 1
    if i < 3:  # Check if there are any attempts left
        guess = int(input(f"You have {3 - i} chances left. Guess again: "))

# Check if the user guessed the number correctly
if num == guess:
    print("Congrats!!! \nYou guessed it right!")
else:
    print(f"Oh! The correct number was {num}.\nBetter luck next time!")
