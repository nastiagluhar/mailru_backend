board = list(range(1, 10))

comb_win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

cells = ['123456789']


def instruction():
    print('This is a Tic-Tac-Toe game. If u wanna make a move press the cell number where do u wanna put ur symbol')


name1 = input('Enter the name of the player whose move will be the first as X: \n')
name2 = input('Enter the name of the player whose move will be the second as O: \n')


def show_board():
    print('_____________')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('_____________')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('_____________')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('_____________')


def validate_input(player_move):
    while True:
        value = input('Where to put ' + player_move + '?')
        if not (value in cells):
            print('Error. Try to put number again')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Cell is taken')
            continue
        board[value - 1] = player_move
        break


def check_win():
    for i in comb_win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    else:
        return False


def start_game():
    counter = 0
    while True:
        show_board()
        if counter % 2 == 0:
            validate_input('X')
        else:
            validate_input('O')
        if counter > 4:
            winner = check_win()
            if winner:
                # show_board()
                print(winner, 'won! Congratulations')
                break
        counter += 1
        if counter > 8:
            show_board()
            print('Draw')
            break


start_game()
