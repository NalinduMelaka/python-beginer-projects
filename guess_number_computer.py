import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > random_num:
            print("Soory, Number is too high. Guess again!")
        elif guess < random_num:
            print("Sorry, Number is too low. Guess again!")
    print("You have won the game")


guess(100)