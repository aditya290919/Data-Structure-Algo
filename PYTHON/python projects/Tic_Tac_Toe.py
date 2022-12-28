from turtle import position
from IPython.display import clear_output


def display_board(board):

    clear_output()

    print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('   |   |')

test_borad=['#','X','O','X','O','X','O','X','O','X']
display_board(test_borad)

def player_input():
    marker=''
    while not (marker=='O' or marker =='X'):
        marker=input("enter player's input(X or O): ").upper()

    if marker=='X':
        return ('x','o')

    else:
        return ('O','X')



def place_marker(board,marker,position):

    board[position]=marker

def is_win(board,mark):

    return ((board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or 
    (board[1]==mark and board[2]==mark and board[3]==mark) or 

    (board[3]==mark and board[5]==mark and board[7]==mark) or 
    (board[1]==mark and board[5]==mark and board[9]==mark) or 

    (board[3]==mark and board[6]==mark and board[9]==mark) or 
    (board[2]==mark and board[5]==mark and board[8]==mark) or 
    (board[1]==mark and board[4]==mark and board[7]==mark))

def space_check(board,position):

    return board[position]==' '


def full_board_check(board):

    for i in range(1,10):

        if space_check(board,i):

            return False

    return True

def positional_argument(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):

        position = int(input("'Enter player's position in board (1 -9): "))

    return position



import random
def player_chance():
    flip=random.randint(1,10)
    if flip==0:
        return 'player1'

    else:
        return 'player2'


def replay():
    play_again=input('Want to play again? (Yes or No)')
    return play_again=='Yes'


print('Welcome to tic tac toe!')

while True:

    the_board=[' ']*10

    player1_marker,player2_marker=player_input()

    turn = player_chance()

    print(turn + ' will go first')

    play_game=input('Want to start a game? (Y or N): ')

    if play_game=='Y':
        game_on=True

    else:
        game_on=False

    while game_on:

        if turn =='player1':

            display_board(the_board)

            position = positional_argument(the_board)

            place_marker(the_board,player1_marker,position)

            if is_win(the_board,player1_marker):

                display_board(the_board)

                print('player 1 wins!')

                game_on=False

            else:
                
                if full_board_check(the_board):
                    display_board(the_board)

                    print('its a tie')

                    game_on=False

                else:
                    turn ='player2'


        else:

            display_board(the_board)

            position = positional_argument(the_board)

            place_marker(the_board,player2_marker,position)

            if is_win(the_board,player2_marker):

                display_board(the_board)

                print('player 2 wins!')

                game_on=False

            else:
                if full_board_check(the_board):
                    display_board(the_board)

                    print('its a tie')

                    game_on=False

                else:
                    turn ='player1'


    if not replay():
        break


                    

            




    





            




    


          






    

