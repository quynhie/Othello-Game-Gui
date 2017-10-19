# Quynh Le
# Othello Game Logic
# Project 4

BLACK = 1
WHITE = 2
NONE = 0

class OthelloGameError(Exception):
    '''raises an exception when an invalid parameter is inputed'''
    pass

class InvalidMoveError(Exception):
    '''raises an exception when an invalid move is made'''
    pass

class GameOverError(Exception):
    '''raises an exception when an attempt is made to
    make a move after the game is over'''
    pass

def create_board(row: int, column: int) -> [[int]]:
    board = []
    for col in range(row):
        board.append([])
        for row in range(column):
            board[-1].append(NONE)
    return board 

class othello_game():
    
    def __init__(self, turn: int, board: [[int]]):
        self._turn = turn
        self._board = board
        
    def check_input(self, tile_row: int, tile_column: int) -> bool:
        '''check whether the input it valid'''
        self._require_valid_row_num(tile_row)
        self._require_valid_column_num(tile_column)
        if self.check_space_valid(tile_row, tile_column):
            return True
        elif self.check_space_valid(tile_row, tile_column) == False:
            raise InvalidMoveError
        
        
    def make_move(self, tile_row: int, tile_column: int) -> 'Othello Game Board':
        '''makes a move in the game: flips tiles, updates board, updates turn'''
        self._require_valid_row_num(tile_row)
        self._require_valid_column_num(tile_column)
        if self.check_space_valid(tile_row, tile_column):
            flipable_tiles = self.flipable_tiles(tile_row, tile_column)
            flip_tiles_on_board = self.flip_tiles(flipable_tiles)
            place_current_tile = self.place_tile(tile_row, tile_column)
            self._board = place_current_tile
            flip_tiles_on_board = self._board
            self._turn = self._flip_turn()
            return self._board
        elif self.check_space_valid(tile_row, tile_column) == False:
            raise InvalidMoveError
        
                
    def print_board(self) -> str:
        '''prints the current board'''
        result = ''
        for row in range((len(self._board))):
            for col in range(len(self._board[row])):
                if self._board[row][col] == NONE:
                    result += '. '
                elif self._board[row][col] == BLACK:
                    result += 'B '
                elif self._board[row][col] == WHITE:
                    result += 'W '
                else:
                    raise OthelloGameError()
            result = result.strip() + '\n'
  
        return result [:-1]
    
    def winner(self, board: [[int]], win: str) -> int:
        '''returns the winner'''
        white = 0
        black = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == BLACK:
                    black += 1
                elif board[row][column] == WHITE:
                    white += 1
        if win == '>':
            if black > white:
                return BLACK 
            elif white > black:
                return WHITE
            else:
                return NONE
        elif win == '<':
            if black < white:
                return BLACK 
            elif white < black :
                return WHITE
            else:
                return NONE
        else:
            raise OthelloGameError()

    def count_black_tiles(self, board: [[int]]) -> int:
        '''counts the number of black tiles'''
        black = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == BLACK:
                    black += 1
        return black

    def count_white_tiles(self, board: [[int]]) -> int:
        '''counts the number of white tiles on the board'''
        white = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == WHITE:
                    white += 1
        return white
    
    def place_tile(self,  row_num: int, column_num: int) -> 'self._board':
        '''places the tile onto the board'''
        self._board[row_num][column_num] = self._turn
        return self._board
    
    def check_all_spaces_valid(self, board: [[int]]) -> bool:
        '''return True if there are still valid spaces on the board'''
        for row in range(len(board)):
            for column in range(len(board[row])):
                if self.check_space_empty(row, column):
                    if self.check_space_valid(row, column):
                        return True                   
   
        return False
        
    def check_space_valid(self, row_num: int, column_num: int) -> bool:
        '''return True if placing a tile in that space is valid'''
        if self.check_space_empty(row_num, column_num):
            if len(self.flipable_tiles(row_num, column_num)) == 0:
                return False
            else:
                return True               
        else:
            return False
    
    def check_space_empty(self, row_num, column_num) -> bool:
        '''returns True if the space is empty'''
        return self._board[row_num][column_num] == NONE

    def flip_tiles(self, flipable_tiles: [[int]]) -> 'self._board':
        '''flips the tiles in the list of flippable tiles'''
        for row in flipable_tiles:
            self._board[row[0]][row[1]] = self._turn
        return self._board

    def flipable_tiles(self, row_num: int, column_num: int) -> list:
       '''creates a list of all the flippable tiles'''
       flipable = []
       
       left = self._left(row_num, column_num)
       diagonal_up_left = self._diagonal_up_left(row_num, column_num)
       diagonal_down_left = self._diagonal_down_left(row_num, column_num)
       right = self._right(row_num, column_num)
       diagonal_up_right = self._diagonal_up_right(row_num, column_num)
       diagonal_down_right = self._diagonal_down_right(row_num, column_num)
       up = self._up(row_num, column_num)
       down = self._down(row_num, column_num)
       
       flipable.extend(left)
       flipable.extend(diagonal_up_left)
       flipable.extend(diagonal_down_left)
       flipable.extend(right)
       flipable.extend(diagonal_up_right)
       flipable.extend(diagonal_down_right)
       flipable.extend(up)
       flipable.extend(down)
       #print('flip: ', filpable)
       return flipable
       
                
    def _left(self, row_num: int, column_num: int) -> list:
        '''creates a list of all the flipable tiles to
        the left of the indicated row & column num'''
        result = []
        convert_row = 0
        convert_column = -1
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('left: ', [row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_column += -1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []

    def _right(self, row_num: int, column_num: int) -> list:
        '''creates a list of all the flipable tiles to
        the right of the indicated row & column num'''
        result = []
        convert_row = 0
        convert_column = 1
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('right: ', [row_num + convert_row, column_num + convert_column])
                result.append(([row_num + convert_row, column_num + convert_column]))
                convert_column += 1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []
    
    def _up(self, row_num: int, column_num: int) -> list:
        '''creates a list of all the flipable tiles above
        of the indicated row & column num'''
        result = []
        convert_row = -1
        convert_column = 0
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('up: ', [row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_row += -1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []

    def _down(self, row_num : int, column_num: int) -> list:
        '''creates a list of all the flipable tiles below
        of the indicated row & column num'''
        result = []
        convert_row = 1
        convert_column = 0
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('down: ',[row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_row += 1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []
    
    def _diagonal_up_left(self, row_num : int, column_num : int) -> list:
        '''creates a list of all the flipable tiles up diagonal & to the left
        of the indicated row & column num'''
        result = []
        convert_row = -1
        convert_column = -1
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('diagonal up left: ', [row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_row += -1
                convert_column += -1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []

    def _diagonal_up_right(self, row_num: int, column_num: int) -> list:
        '''creates a list of all the flipable tiles up diagonal & to the right
        of the indicated row & column num'''
        result = []
        convert_row = -1
        convert_column = 1
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('diagonal up left: ',[row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_row += -1
                convert_column += 1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []

    def _diagonal_down_right(self, row_num: int, column_num: int) -> list:
        '''creates a list of all the flipable tiles down diagonal & to the right
        of the indicated row & column num'''
        result = []
        convert_row = 1
        convert_column = 1
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('diagonal down right: ', [row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_row += 1
                convert_column += 1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []

    def _diagonal_down_left(self, row_num: int, column_num: int) -> list:
        '''creates a list of all the flipable tiles up diagonal & to the right
        of the indicated row & column num'''
        result = []
        convert_row = 1
        convert_column = -1
        while self._check_range(row_num + convert_row, column_num + convert_column):
            if self._board[row_num + convert_row][column_num + convert_column] == self._flip_turn():
                #print('diagpnal down left: ',[row_num + convert_row, column_num + convert_column])
                result.append([row_num + convert_row, column_num + convert_column])
                convert_row += 1
                convert_column += -1
            elif self._board[row_num + convert_row][column_num + convert_column] == self._turn:
                return result
            else:
                return []
        return []
    def _check_range(self, row_num: int, column_num: int) -> bool:
        '''checks to see if the column num & row num are inside the range'''
        if 0 <= column_num < len(self._board[1]) and 0 <= row_num < len(self._board):
            return True
        else:
            return False
    
    def _flip_turn(self) -> int:
        '''returns the opposite turn'''
        if self._turn == BLACK:
            return WHITE
        else:
            return BLACK
        
    def _require_game_not_over(self, board: [[int]], win: str) -> None:
        '''raises an error if the game is already over'''
        if self.winner(board, win) == NONE or self.winner(board, win) == WHITE or self.winner(board, win) == BLACK:
            pass
        else:
            raise GameOverError()
        
    def _require_valid_column_num(self, column_num: int) -> None:
        ''' raises error if the column num is not an int or within the board'''
        if type(column_num) != int or not self._is_valid_column_num(column_num):
            raise ValueError
        
    def _require_valid_row_num(self, row_num: int) -> None:
        '''raises error if the column num is not an int or within the board'''
        if type(row_num) != int or not self._is_valid_row_num(row_num):
            raise ValueError
    
    def _is_valid_column_num(self, column_num: int) -> bool:
        '''returns True if the column num is a valid num & False if not'''
        return 0 <= column_num < len(self._board[1])
    
    def _is_valid_row_num(self, row_num: int) -> bool:
        '''returns True if the row num is a valid num & False if not'''
        return 0 <= row_num < len(self._board) 

