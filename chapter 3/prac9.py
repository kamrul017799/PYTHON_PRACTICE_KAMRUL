#Create a simple Rock, Paper, Scissors game where the user can keep playing until they choose to quit. Use random and a loop.
import random , sys
print('rock as r, paper as p, scissors as s')

win = 0
loss = 0
tie = 0
while True:  # The main game loop
    print( (win, loss, tie))
    while True:
        print('enter you r,p,s,q')
        plyaer_move = input()
        if plyaer_move == 'q':
            sys.exit()
        elif plyaer_move == 'r' or plyaer_move == 'p' or plyaer_move =='s':
            break 

    if plyaer_move == 'r':
        print('rock')
    elif plyaer_move == 'p':
        print('paper')
    elif plyaer_move == 's':
        print('sessior')


    print('computer choose')
    computer = random.randint(1,3)
    if computer == 1:
        computer = 'r'
        print('rock')

    elif computer == 2:
        computer = 'p'
        print('paper')
    elif computer == 3:
        computer = 's'
        print('sessior')


    if plyaer_move == computer:
        print('you tie')
        tie = tie + 1
    elif plyaer_move == 'r' and computer == 'p':
        print('you win')
        win= win +1
    elif plyaer_move == 'p' and computer =='s':
        print('you win')
        win = win+1
    elif plyaer_move == 's' and computer == ' r':
        print('you win')
        win = win +1
    elif plyaer_move == 'p' and computer == 'r':
        print('you loss')
        loss= loss+1
    elif plyaer_move == 's' and computer== 'p':
        print('you loss')
        loss = loss +1
    elif plyaer_move == 'p' and computer == 's':
        print(' you loss')
        loss = loss + 1
    
         
