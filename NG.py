import random

num = random.randint(1, 100)# Generating a random number between 1 and 100

guess = int(input("Guess a number between 1 to 100: "))# Asking the user to guess the number

# Loop until the user guesses the correct number
i=0 

while i<3:
    if num > guess:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")

    guess = int(input("You have only "+i+" chances Guess again: "))# Prompt the user to guess again
    i+=1

print("Congrats!!! \nYou guessed it right!")# Congratulate the user when they guess correctly
