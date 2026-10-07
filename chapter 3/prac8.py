#Create a simple number guessing game where the computer chooses a random number between 1 and 20, and the user gets 5 attempts to guess it.
import random
sec_num = random.randint(1,20)
print(" i assmue a number")

for num_gauses in range(1,6):
    guess = int(input())

    if guess < sec_num:
        print(' to low')
    elif guess > sec_num:
        print('to high')
    else:
        break
if guess == sec_num:
    print('youer guess is right')
else:
    print('better luck for next time')

