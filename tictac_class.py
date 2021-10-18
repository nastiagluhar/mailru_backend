class TicTacGame:

    def __init__(self, player_move, validate_input, name1, name2):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.comb_win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        self.counter = 0
        self.player_move = player_move
        self.validate_input = validate_input
        self.name1 = name1
        self.name2 = name2

    def show_board(self):
        print('This is a Tic-Tac-Toe game. If u wanna make a move press the cell number where do u wanna put ur symbol')
        self.name1 = input('Enter the name of the player whose move will be the first as X: \n')
        self.name2 = input('Enter the name of the player whose move will be the second as O: \n')

        print('_____________')
        print('|', self.board[0], '|', self.board[1], '|', self.board[2], '|')
        print('_____________')
        print('|', self.board[3], '|', self.board[4], '|', self.board[5], '|')
        print('_____________')
        print('|', self.board[6], '|', self.board[7], '|', self.board[8], '|')
        print('_____________')

    def validate_input(self):
        while True:
            value = input('Where to put ' + self.player_move + '?')
            if not (value in '123456789'):
                print('Error. Try to put number again')
                continue
            value = int(value)
            if str(self.board[value - 1]) in 'XO':
                print('Cell is taken')
                continue
            self.board[value - 1] = self.player_move
            break

    def check_win(self):
        for i in self.comb_win:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                return self.board[i[0]]
        else:
            return False

    def start_game(self):
        self.counter = 0
        while True:
            self.show_board()
            if self.counter % 2 == 0:
                self.validate_input('X')
            else:
                self.validate_input('O')
            if self.counter > 3:
                winner = self.check_win()
                if winner:
                    self.show_board()
                    print(winner, 'won! Congratulations')
                    break
            self.counter += 1
            if self.counter > 8:
                self.show_board()
                print('Draw')
                break


#if __name__ == '__main__':
    #Game = TicTacGame()
    #Game.start_game()
