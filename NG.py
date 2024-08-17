import random

num = random.randint(1, 100)# Generating a random number between 1 and 100

guess = int(input("Guess a number between 1 to 100: "))# Asking the user to guess the number

# Loop until the user guesses the correct number
while num != guess:
    if num > guess:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
    # Prompt the user to guess again
    guess = int(input("Guess again: "))