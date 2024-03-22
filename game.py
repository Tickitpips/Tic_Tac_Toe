from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None #keep track of winner

    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]:
            print('| '+ ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(('| '+ ' | '.join(row) + ' |'))

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #for (i, spot) in enumerate(self.board):
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
        # or return len(self.available_moves())
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to a letter)
        # then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere
        #  checking the row
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square%3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        #but only if the square is an even number (0, 2,4,6,8)
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False    



def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game (the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'x'   # starting letter
    #iterate while the game still has many squares
    #we dont have to worry about the winner since we 
    #will just return that which breaks the loop
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('')  #just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!!')
                return letter

            #after we make our move, we need to alternate letters. 
            letter = 'o' if letter == 'x' else 'x'

        if print (game):
           time.sleep(0.8)

    if print_game:
            print('It\'s a tie')

"""if __name__ == '__main__':
    x_player = RandomComputerPlayer('x')
    o_player = GeniusComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)"""

#To check the win rate of the AI, 
if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    
    for i in range(1000):
        x_player = RandomComputerPlayer('x')
        o_player = GeniusComputerPlayer('o')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'x':
            x_wins+=1
        elif result == 'o':
            o_wins+=1
        else:
            ties+=1
    accuracy = o_wins*100/1000
    print(f"After 1000 iterations we see {x_wins} x wins, {o_wins} and {ties} ties and that is a {accuracy} win accuracy")
   
