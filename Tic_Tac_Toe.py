# Console based Tic-Tac-Toe
from random import *

print("Welcome to Triple T")
board = []
for i in range(10):
    board.append(' ')

n = 1   # use n to alter the players turn one by one.
p1 = ' '
p2 = ' '

'''select a random player to start. the game.'''
a = randint(0, 1)

print("Player 1 Turn: ")
while p1 != 'X' and p1 != 'O':
    p1 = input('Player 1 Enter choice:(O or X)').upper()

if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'

def win_tst(board, check):    # whether player is won or not ??
    return (board[1] == check and board[2] == check and board[3] == check or\
            board[4] == check and board[5] == check and board[6] == check or\
            board[7] == check and board[8] == check and board[9] == check or\
            board[1] == check and board[4] == check and board[7] == check or\
            board[2] == check and board[5] == check and board[8] == check or\
            board[3] == check and board[6] == check and board[9] == check or\
            board[1] == check and board[5] == check and board[9] == check or\
            board[7] == check and board[5] == check and board[3] == check)

def tst_board(board):
    '''displays the board'''
    print("\n" * 10)
    print('   '+board[7]+ ' | '+board[8]+' | '+board[9])
    print(' -------------')
    print('   '+board[4]+ ' | '+board[5]+' | '+board[6])
    print(' -------------')
    print('   '+board[1]+ ' | '+board[2]+' | '+ board[3])
    # call win_tst here!

    if win_tst(board, 'X'):
        if p1 == 'X':
            print("player 1 won")
            exit()
        else:
            print("player 2 won")
            exit()
    elif win_tst(board, 'O'):
        if p1 =='O':
            print("player 1 won")
            exit()
        else:
            print("player 2 won")
            exit()

    else:
        for i in range(1, 10):
            if board[i] == ' ':
                break
        else:
            print("It is a Tie")
            exit()

tst_board(board)

if a == 0:
    while n <= 9:
        if n % 2 == 0: # p1 will start first.
            key = int(input("Enter place Player 1:"))
            if board[key] == ' ':
                board[key] = p1
            else:
                while board[key] != ' ':
                    print("Already allocated....")
                    key = int(input("Enter new value:"))
                board[key] = p1

            n += 1
            tst_board(board)
        else:
            key = int(input("Enter place Player 2:"))
            if board[key] == ' ':
                board[key] = p2
            else:
                while board[key] != ' ':
                    print("Already allocated....")
                    key = int(input("Enter new value:"))

                board[key] = p2

            n += 1
            tst_board(board)
else:
    while n <= 9:
        if n % 2 == 0:  # p2 will start first.
            key = int(input("Enter place Player 2:"))
            if board[key] == ' ':
                board[key] = p2
            else:
                while board[key] != ' ':
                    print("Already allocated....")
                    key = int(input("Enter new value:"))

                board[key] = p2

            n += 1
            tst_board(board)
        else:
            key = int(input("Enter place Player 1:"))
            if board[key] == ' ':
                board[key] = p1
            else:
                while board[key] != ' ':
                    print("Already allocated....")
                    key = int(input("Enter new value:"))

                board[key] = p1

            n += 1
            tst_board(board)
