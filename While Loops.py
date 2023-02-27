User Input

while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        

Guessing Game

import random

number = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the right number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
