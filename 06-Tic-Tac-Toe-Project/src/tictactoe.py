# define the board an one dimensional array

import random


class TicTacToe:
    def __init__(self, ):
        """ 
        Initialize the Tic Tac Toe game with an empty board 
        and select the first player randomly from 'X' or 'O'.
        """
        self.board = [' '] * 10     # list(map(str, range(10)))    # multiply to 10, which starts from 1 ( 0th index is not used)
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        """
        Randomly select the first player.

        :return: A string indicating which player goes first ('x' or 'O').  
        """
        return random.choice(['x' , 'O'])

    
    def show_board(self) -> None:
        """ 
        Display the current state of the board to the console. 
        """
        print('\n')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-----')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-----')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')

    def swap_player_turn(self) -< str:
        """  
        Swap the turn from the current player to the other.
        
        :return: A string indicating which player's turn is next ('x' or 'O').
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn

    def is_board_filled(self) -> bool: 
        """ 
        Check if the board has no empty spots lefts.
        :return: A boolean value indicating whether the board is filled. 
        """  
        return ' ' not in self.board[1:]    # if this empty is not from 1 to the end.

    def fix_spot(self, cell: int, player: str) -> None:
        """
        Place the player's mark on the specified cell.

        :param cell: An integer indicating the cell number (1-9).
        :param player: A string indicating the player's mark ('x' or 'O').
        """
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        """  
        Check if the specified player has won the game.

        :param player: A string indicating the player's mark ('x' or 'O').
        :return: A boolean value indicating whether the player has won.
        """
        win_combination = [
        [1,2,3], [4,5,6], [7,8,9], # rows
        [1,4,7], [2,5,8], [3,6,9], # columns
        [1,5,9], [3,5,7] # diagonals
        ]
        for combination in win_combination:
            if all([self.board[cell] == player for cell in combination]):
                return True

        return False

    def start(self) -> None:
        """  
        Start the game loop untill there is a winner or a draw.
        """
        while True:
            self.show_board()
            print(f"turn of player {self.player_turn}")
            cell = int(input('Enter cell number from 1 to 9: '))

            if cell in range(1, 10) and self.board[cell] == ' ':
                self.fix_spot(cell, self.player_turn)

                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f"player {self.player_turn} won!")
                    break

                if self.is_board_filled():
                    self.show_board()
                    print("Draw!")
                    break

                self.swap_player_turn()

            else:
                print("Invalid cell number or cell is already occupied.")


if __name__ == '__main__':
    game = TicTacToe()
    game.start()

    