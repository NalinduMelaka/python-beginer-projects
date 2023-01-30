import random

def rps():
    user = input("Enter 'r' for rock 'p' for paper 's' for scissors :")
    computer = random.choice(['r','p','c'])
    if user==computer:
        return("tie")
    if win(user,computer):
        return "you won"
    return "you lose"

# r&c=r p&c=c r&p=p
def win(player,comp):
    if (player=='r' and comp=='c') or (player=='p' and comp=='r') or (player=='c' and comp=='p'):
        return True

print(rps())


