import random

rando = random.randint(1, 100)

a = int(input('Guess a number \n'))

while a != rando:
    if a > rando: 
        print('Too high! Try again')
        a = int(input('Guess a number \n'))
    elif a < rando:
        print('Too low. Try again ')
        a = int(input('Guess a number \n'))

print("Correct! ")
