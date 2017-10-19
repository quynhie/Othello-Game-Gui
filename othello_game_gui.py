# Quynh Le
# 27537272
# Project 5
# Othello Gui

import othello_gamelogic
import tkinter
import point

DEFAULT_FONT = ('Helvetica', 14)

class GameSetUp():
    
    def __init__(self):
        
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0,0)

        greeting_label = tkinter.Label(
            master = self._root_window,
            text = 'Welcome to the Full Othello Game! ',
            font = DEFAULT_FONT)
        
        greeting_label.grid(
            row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        intructions_label = tkinter.Label(
            master = self._root_window,
            text = 'Please enter in the following inputs:',
            font = DEFAULT_FONT)
        intructions_label.grid(
            row = 1 , column = 0, padx = 10, pady = 10, sticky = tkinter.E)

        # row
        self._row_input = tkinter.Spinbox(
            master = self._root_window, values = ( 4,6,8,10,12,14,16))
        self._row_input.grid(
            row = 2 , column = 1, padx= 10 , pady =10, sticky = tkinter.N)
        self._row_label = tkinter.Label(
            master = self._root_window, text = 'Number of Rows: ',
            font = DEFAULT_FONT)
        self._row_label.grid(
            row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        # column
        self._column_input = tkinter.Spinbox(
            master = self._root_window, values = ( 4,6,8,10,12,14,16))
        self._column_input.grid(
            row = 3 , column = 1 ,padx = 10, pady = 10, sticky = tkinter.E)
        self._column_label = tkinter.Label(
            master = self._root_window, text = 'Number of Columns: ',
            font = DEFAULT_FONT)
        self._column_label.grid(
            row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        
        # starting player
        self._starting_player_input = tkinter.Spinbox(
            master = self._root_window, values = ( 'B', 'W'))
        self._starting_player_input.grid(
            row = 4 , column = 1 ,padx = 10, pady = 10, sticky = tkinter.E)
        self._starting_player_label = tkinter.Label(
            master = self._root_window, text = 'Starting Player: ',
            font = DEFAULT_FONT)
        self._starting_player_label.grid(
            row = 4 , column = 0 ,padx = 10, pady = 10, sticky = tkinter.W)

        # win option
        self._win_option_input = tkinter.Spinbox(
            master = self._root_window, values = ( 'the Most Tiles Win',
                                                   'the Least Tiles Win'))
        self._win_option_input.grid(
            row = 5 , column = 1 ,padx = 10, pady = 10, sticky = tkinter.E)
        self._win_option_label = tkinter.Label(
            master = self._root_window, text = 'How the Game is Played: ',
            font = DEFAULT_FONT)
        self._win_option_label.grid(
            row = 5 , column = 0 ,padx = 10, pady = 10, sticky = tkinter.W)

        # start & cancel buttons
        button_frame = tkinter.Frame(master = self._root_window)
        button_frame.grid( row = 6, column = 0,columnspan = 2, sticky = tkinter.E + tkinter.S )
        start_button = tkinter.Button(
            master = button_frame, text = 'Start Game', font = DEFAULT_FONT,
            command = self._on_start_button)
        start_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)
        cancel_button.grid( row = 0 , column = 1, sticky = tkinter.E)

        self._root_window.rowconfigure(6, weight = 1)
        self._start_button_clicked = False

    def _get_column(self) -> int :
        '''returns the number of columns'''
        #print(self.column )
        return self._column 
    
    def _get_row(self) -> int :
        '''returns the number of rows'''
        #print(self._row)
        return self._row
    
    def _get_starting_player(self) -> str:
        '''returns the starting player'''
        if self._starting_player == 'B':
            self._starting_player = 1
            return self._starting_player
        elif self._starting_player == 'W':
            self._starting_player = 2
            return self._starting_player
    
    def _get_win_option(self) -> str:
        '''returns the win option '''
        if self._win_option == 'the Most Tiles Win':
            self._win_option = '>'
            return self._win_option
        elif self._win_option == 'the Least Tiles Win':
            self._win_option = '<'
            return self._win_option 
    
    def _on_cancel_button(self) -> None:
        '''destroys the window'''
        self._root_window.destroy()
        
    def _on_start_button(self) -> None:
        '''grabs the inputs'''
        self._start_button_clicked = True
        self._row = int(self._row_input.get())
        #print(self._row)
        self._column = int(self._column_input.get())
        #print(self._column)
        self._starting_player = self._starting_player_input.get()
        #print(self._get_starting_player())
        self._win_option = self._win_option_input.get()
        #print(self._get_win_option())
        self._root_window.destroy()
    
    def run(self):
        self._root_window.mainloop()

class OthelloGame():
    
    def __init__(self):
        game_input = GameSetUp()
        game_input.run()
        
        # game inputs
        self._total_columns = game_input._get_column()
        self._total_rows = game_input._get_row()
        self._win_option = game_input._get_win_option()
        self._starting_player = game_input._get_starting_player()
        self._board = othello_gamelogic.create_board(self._total_rows, self._total_columns)

        # game logic 
        self._othello_gamelogic = othello_gamelogic.othello_game(self._starting_player, self._board)
        self._starting_player = self._othello_gamelogic._turn
        
        # canvas
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 600, height = 600,
            background = 'pale violet red')
        self._canvas.grid(
            row = 0, column = 0, padx = 50, pady = 20, 
            sticky = tkinter.N  + tkinter.W + tkinter.E)
        
        # next button
        button_frame = tkinter.Frame(master = self._root_window)
        button_frame.grid(row = 2, column = 0, padx = 10, pady = 10,
                          sticky = tkinter.S + tkinter.E)
        self._next_button = tkinter.Button(
            master = button_frame, text = 'Next', font = DEFAULT_FONT,
            command = self._next_button_clicked)
        self._next_button.grid( row = 4, column = 0,
                                 sticky =  tkinter.E)
        
        # The changeable labels for the game
        self._current_player_label(self._starting_player)
        self._winner = tkinter.StringVar()
        self._winner.set('WINNER: -- ')
        winner_label = tkinter.Label(
                master = self._root_window, textvariable =self._winner,
                font = DEFAULT_FONT)
        winner_label.grid(row = 2, column = 0, sticky = tkinter.S)
        self._score_board = tkinter.IntVar()
        self._score_board.set('Black: 0  White: 0')
        score_board_label = tkinter.Label(
            master = self._root_window, textvariable = self._score_board,
            font = DEFAULT_FONT)
        score_board_label.grid(row = 1 , column = 0, sticky = tkinter.S)

        # configuring rows & columns
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 0) #to get the 'next' button to stay on the canvas when configured. 
        self._root_window.columnconfigure(0, weight = 1)

        # binding events
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        # important variables used in the other functions
        self._start_clicked = False
        self._clicked_list = []

    def _current_player_label(self, player: int) -> None:
        '''creates a label indicating the current player'''
        self._current_player_text = tkinter.StringVar()
        if player == othello_gamelogic.BLACK:
            self._current_player_text.set('Place Black Tiles')
        else:
            self._current_player_text.set('Place White Tiles')
        current_player_label = tkinter.Label(
            master = self._root_window, textvariable = self._current_player_text,
            font = DEFAULT_FONT)
        current_player_label.grid(row = 0, column = 0, sticky = tkinter.N)
        
    def _winner_label(self) -> None:
        '''determines the winner & creates a label stating the winner'''
        winner = self._othello_gamelogic.winner(self._board, self._win_option)
        if winner == othello_gamelogic.BLACK:
            self._winner.set('WINNER: BLACK')
        elif winner == othello_gamelogic.WHITE:
            self._winner.set('WINNER: WHITE')
        elif winner == othello_gamelogic.NONE:
            self._winner.set("WINNER: IT'S A TIE!")

        
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''redraws the lines and tiles when the canvas is resized'''
        self._canvas.delete(tkinter.ALL)
        self._draw_lines()
        self._redraw_all_tiles()
        
    def _on_canvas_clicked(self, event:tkinter.Event) -> None:
        '''draws the tiles where the canvas is clicked to play the game'''
        if self._start_clicked == False:
            mouse_location = self._mouse_location(event)
            self._clicked_list.append(mouse_location)
           
            self._board[mouse_location[0]] [mouse_location[1]] = self._othello_gamelogic._turn
    
            for tile in self._clicked_list:
                self._draw_tiles(tile[0], tile[1])
        else:
            self._play_game(event)
         
    def _mouse_location(self, event: tkinter.Event) -> 'tuple of row & column':
        '''returns a tuple of the location of the mouse click'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        click_point = point.from_pixel(
            event.x, event.y, canvas_width, canvas_height)
        frac_x, frac_y = click_point.frac()
        
        for row in range(self._total_rows +1) :
            for column in range(self._total_columns + 1):
                if frac_x < column/self._total_columns and frac_y < row/self._total_rows:
                    return [row -1, column -1]

    def _next_button_clicked(self) -> None:
        ''' flips the turn when the button is clicked & creates a start button'''
        self._othello_gamelogic._turn = self._othello_gamelogic._flip_turn()
        self._current_player_label(self._othello_gamelogic._turn)
        self._next_button.destroy()
        self._start_button = tkinter.Button(
            master = self._root_window, text = 'Start', font = DEFAULT_FONT,
            command = self._start_button_clicked)
        self._start_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.E)
        
    def _start_button_clicked(self) -> None:
        ''' flips the turn back to the correct player, starts the game & creates a quit button'''
        self._othello_gamelogic._turn = self._othello_gamelogic._flip_turn()
        self._start_clicked = True
        self._current_player_label(self._othello_gamelogic._turn)
        self._start_button.destroy()
        self._quit_button = tkinter.Button(
            master = self._root_window, text = 'Quit', font = DEFAULT_FONT,
            command = self._quit_button_clicked)
        self._quit_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.E)
        total_black_tiles = self._othello_gamelogic.count_black_tiles(self._board)
        total_white_tiles = self._othello_gamelogic.count_white_tiles(self._board)
        self._score_board.set('Black: {}  White: {}'.format(total_black_tiles, total_white_tiles))
        self._check_for_valid_moves()

            
    def _quit_button_clicked(self):
        '''destroys the entire window when quit is clicked'''
        self._root_window.destroy()
        
    def _play_game(self, event: tkinter.Event) -> None:
        '''implements the game logic to play the game'''
        tile_row, tile_column = self._mouse_location(event)
        if self._othello_gamelogic.check_all_spaces_valid(self._board) == False:
            self._turn = self._othello_gamelogic._flip_turn()
            if self._othello_gamelogic.check_all_spaces_valid(self._board):
                  self._current_player_label(self._othello_gamelogic._turn)
                  self._play_game(event)

        elif self._othello_gamelogic.check_all_spaces_valid(self._board):
            try:
                self._othello_gamelogic.make_move(tile_row, tile_column)
                self._current_player_label(self._othello_gamelogic._turn)
                total_black_tiles = self._othello_gamelogic.count_black_tiles(self._board)
                total_white_tiles = self._othello_gamelogic.count_white_tiles(self._board)
                self._score_board.set('Black: {}  White: {}'.format(total_black_tiles, total_white_tiles))
                self._redraw_all_tiles()
                        
            except othello_gamelogic.InvalidMoveError:
                pass
            except othello_gamelogic.GameOverError:
                pass
        
        if self._othello_gamelogic.check_all_spaces_valid(self._board) == False:
            self._turn = self._othello_gamelogic._flip_turn()
            if self._othello_gamelogic.check_all_spaces_valid(self._board) == False:
                self._winner_label()
                
    def _check_for_valid_moves(self) -> None:
        '''check for any valid turn fo rcurrent player
        & correctly places a label indicating the current player's turn in GUI'''
    
        if self._othello_gamelogic.check_all_spaces_valid(self._board):
            self._current_player_label(self._othello_gamelogic._turn)
        elif self._othello_gamelogic.check_all_spaces_valid(self._board)== False:
            self._othello_gamelogic._turn = self._othello_gamelogic._flip_turn()
            if self._othello_gamelogic.check_all_spaces_valid(self._board):
                self._current_player_label(self._othello_gamelogic._turn)
            else:
                self._winner_label()
                
    def _redraw_all_tiles(self) -> None:
        '''redraws all the tiles on the board'''
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                self._draw_tiles(row, column)
    
    def _draw_lines(self):
        '''draws the lines for the game board'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
  
        for col in range(self._total_columns):
            self._canvas.create_line(
                canvas_width/self._total_columns * col, canvas_height * 0,
                canvas_width/self._total_columns * col, canvas_height * col,
                width = 4, fill = 'misty rose')
            
        for r in range(self._total_rows):
            self._canvas.create_line(
                canvas_width * 0, canvas_height/self._total_rows * r,
                canvas_width * r, canvas_height/self._total_rows * r,
                width = 3, fill = 'misty rose')
            
    def _draw_tiles(self, clicked_row: int, clicked_column: int):
        '''draws the game tiles'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        if self._board[clicked_row][clicked_column] == othello_gamelogic.BLACK:
            self._canvas.create_oval(canvas_width/self._total_columns * clicked_column,
                                     canvas_height/self._total_rows *clicked_row,
                                     canvas_width/self._total_columns * (clicked_column+1),
                                     canvas_height/self._total_rows * (clicked_row +1),
                                     width = 3, fill = 'black', outline = 'black')
            
        elif self._board[clicked_row][clicked_column] == othello_gamelogic.WHITE:
            self._canvas.create_oval(canvas_width/self._total_columns * clicked_column,
                                     canvas_height/self._total_rows *clicked_row,
                                     canvas_width/self._total_columns * (clicked_column+1),
                                     canvas_height/self._total_rows * (clicked_row +1),
                                     width = 3, fill = 'white', outline = 'white')


    def run(self):
        self._root_window.mainloop()


if __name__ == '__main__':
    OthelloGame().run()

