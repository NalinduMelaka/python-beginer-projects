import random

def computer_guess(x):
    low=1
    high=x
    user_feedback=""
    while user_feedback != 'c':
        if low != high:
            guess= random.randint(low,high)
        else:
            guess = low
        user_feedback= input(f"Is the guess {guess} is too low enter 'L', too high enter 'H', equal enter 'C'?").lower()
        if user_feedback == 'h':
            high = guess - 1
        elif user_feedback == 'l':
            low = guess + 1
    print(f"congratulation, computer guess the number {guess}")

computer_guess(100)