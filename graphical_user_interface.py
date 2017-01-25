### MODULES/LIBRARIES ###

import tkinter
import game_logic
import point

### CONSTANTS ###

DEFAULT_FONT = ('Calibri', 25)

### CLASSES ###

class StartGame:
    def __init__(self):
        self._root_window = tkinter.Tk()
        
        self._input_list = []
        
        start_game_button = tkinter.Button(
            master = self._root_window, text = 'Start Game', font = ('Calibri', 50),
            command = self._start_new_game)

        start_game_button.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = tkinter.S + tkinter.N +tkinter.E + tkinter.W)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def run(self) -> None:
        'Runs the mainloop of the tkinter window.'
        self._root_window.mainloop()
            
    def _start_new_game(self) -> None:
        'Once Start Game button is clicked, GameSetUpDialog will pop up. Information from the dialog box will be saved and the Start Game button will be destroyed.' 
        dialog = GameSetUpDialog()
        dialog.show()
        if dialog.was_ok_clicked():
            row = int(dialog._row)
            self._input_list.append(row)
            column = int(dialog._column)
            self._input_list.append(column)
            player_first = dialog._player_first
            if player_first == 'Black':
                player_first = 1
            else:
                player_first = 2
            self._input_list.append(player_first)
            color_top_left = dialog._color_top_left
            if color_top_left == 'Black':
                color_top_left = 1
            else:
                color_top_left = 2
            self._input_list.append(color_top_left)
            game_won = dialog._game_won
            if game_won == 'More discs':
                game_won = '>'
            else:
                game_won = '<'
            self._input_list.append(game_won)
            self._root_window.destroy()



class GameSetUpDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        title_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Game Set-Up', font = DEFAULT_FONT)

        title_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.S)

        row_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Number of rows:', font = DEFAULT_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E)

        row_list = (4, 6, 8, 10, 12, 14, 16)
        self._row_variable = tkinter.StringVar()
        self._row_variable.set(4)
        
        self._row_option = tkinter.OptionMenu(
            self._dialog_window, self._row_variable, *row_list)

        self._row_option.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W)
        
        column_list = (4, 6, 8, 10, 12, 14, 16)
        self._column_variable = tkinter.StringVar()
        self._column_variable.set(4)
        
        column_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Number of columns:', font = DEFAULT_FONT)

        column_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E)

        self._column_option = tkinter.OptionMenu(
            self._dialog_window, self._column_variable, *column_list)

        self._column_option.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W)

        player_first_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Which player moves first?', font = DEFAULT_FONT)

        player_first_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E)

        player_first_list = ('Black', 'White')
        self._player_first_variable = tkinter.StringVar()
        self._player_first_variable.set('Black')

        self._player_first = tkinter.OptionMenu(
            self._dialog_window, self._player_first_variable, *player_first_list)

        self._player_first.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W)
        
        color_top_left_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Color in top-left position?', font = DEFAULT_FONT)

        color_top_left_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E)

        color_top_left_list = ('Black', 'White')
        self._color_top_left_variable = tkinter.StringVar()
        self._color_top_left_variable.set('Black')

        self._color_top_left = tkinter.OptionMenu(
            self._dialog_window, self._color_top_left_variable, *color_top_left_list)

        self._color_top_left.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W)

        game_won_label = tkinter.Label(
            master = self._dialog_window,
            text = 'How game is won:', font = DEFAULT_FONT)
        
        game_won_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E)

        game_won_list = ('More discs', 'Fewer discs')
        self._game_won_variable = tkinter.StringVar()
        self._game_won_variable.set('More discs')

        self._game_won = tkinter.OptionMenu(
            self._dialog_window, self._game_won_variable, *game_won_list)

        self._game_won.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 0)
        self._dialog_window.rowconfigure(2, weight = 0)
        self._dialog_window.rowconfigure(3, weight = 0)
        self._dialog_window.rowconfigure(4, weight = 0)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False

        self._row = self._row_variable
        self._column = self._column_variable
        self._player_first = self._player_first_variable
        self._color_top_left = self._color_top_left_variable
        self._game_won = self._game_won_variable

    def show(self) -> None:
        'Gives control to the dialog box.'
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        'Returns a boolean if the ok button was clicked.'
        return self._ok_clicked

    def _on_ok_button(self) -> None:
        'Saves information and destroys dialog window when ok button is clicked.'
        self._ok_clicked = True
        self._row = self._row_variable.get()
        self._column = self._column_variable.get()
        self._player_first = self._player_first_variable.get()
        self._color_top_left = self._color_top_left_variable.get()
        self._game_won = self._game_won_variable.get()
        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        'Destroys dialog window when cancel button is clicked.'
        self._dialog_window.destroy()
    


class OthelloGUI:
    def __init__(self, settings_list: list):
        self._root_window = tkinter.Tk()
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 400, height = 400,
            background = '#FF7D63')

        self._canvas.grid(
            row = 2, column = 0,
            padx = 10, pady = 10, 
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._game = game_logic.Othello(
            settings_list._input_list[0],
            settings_list._input_list[1],
            settings_list._input_list[2],
            settings_list._input_list[3],
            settings_list._input_list[4])

        initial_count = self._game.count_discs()
        self._score_text = tkinter.StringVar()
        self._score_text.set('BLACK: {}   |   WHITE: {}'.format(initial_count[0], initial_count[1]))

        self._turn_and_winner_text = tkinter.StringVar()
        turn = self._game._turn
        if turn == 1:
            turn = 'BLACK'
        else:
            turn = 'WHITE'
        self._turn_and_winner_text.set('{}\'S TURN'.format(turn))

        title_label = tkinter.Label(
            master = self._root_window,
            text = 'OTHELLO FULL VERSION',
            font = DEFAULT_FONT)
        
        title_label.grid(row = 0, column = 0, sticky = tkinter.N)

        score_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._score_text,
            font = DEFAULT_FONT)
        
        score_label.grid(row = 1, column = 0, sticky = tkinter.N)

        turn_and_winner_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._turn_and_winner_text, font = DEFAULT_FONT)
        
        turn_and_winner_label.grid(row = 3, column = 0, sticky = tkinter.N)
        
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)

        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._canvas.bind('<Configure>', self._on_canvas_resized)

    def run(self) -> None:
        'Runs the mainloop of the tkinter window.'
        self._root_window.mainloop()

    def _on_canvas_resized(self, event:tkinter.Event) -> None:
        'When the Canvas size changes, redraws the board and pieces.'
        self._draw_board()

    def _draw_board(self) -> None:
        'Draws the horizonal lines, vertical lines, and pieces of the board.'
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        horizontal_lines = self._game._rows + 1
        vertical_lines = self._game._columns + 1
        for column in range(vertical_lines):
            self._canvas.create_line(column * (canvas_width/(self._game._columns)), 0,
                                     column * (canvas_width/(self._game._columns)), canvas_height,
                                     fill = 'black')
        for row in range(horizontal_lines):
            self._canvas.create_line(0, row * (canvas_height/(self._game._rows)),
                                     canvas_width, row * (canvas_height/(self._game._rows)),
                                     fill = 'black')
        self._draw_pieces()
        
        new_count = self._game.count_discs()
        self._score_text.set('BLACK: {}  |  WHITE: {}'.format(new_count[0], new_count[1]))
        
        turn = self._game._turn
        if turn == 1:
            turn = 'BLACK'
        else:
            turn = 'WHITE'
        self._turn_and_winner_text.set('{}\'S TURN'.format(turn))
        
        game_over = self._game.game_over()
        turn = self._game._turn
        if turn == 1:
            turn = 'BLACK'
        else:
            turn = 'WHITE'
        self._turn_and_winner_text.set('{}\'S TURN'.format(turn))
        if game_over:
            winner = self._game.winner()
            if winner == 0:
                winner = 'NONE'
            elif winner == 1:
                winner = 'BLACK'
            elif winner == 2:
                winner = 'WHITE'
            self._turn_and_winner_text.set('WINNER: {}'.format(winner))
                    
    def _draw_pieces(self) -> None:
        'Draws the game pieces from the Othello game state.'
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for lst in range(len(self._game._game_state)):
            for item in range(len(self._game._game_state[lst])):
                if self._game._game_state[lst][item] == 1:
                    self._canvas.create_oval((item/self._game._columns) * width,
                                             (lst/self._game._rows) * height,
                                             ((item + 1)/self._game._columns) * width,
                                             ((lst + 1)/self._game._rows) * height,
                                             outline = '#FF7D63', fill = 'black')
                elif self._game._game_state[lst][item] == 2:
                    self._canvas.create_oval((item/self._game._columns) * width,
                                             (lst/self._game._rows) * height,
                                             ((item + 1)/self._game._columns) * width,
                                             ((lst + 1)/self._game._rows) * height,
                                             outline = '#FF7D63', fill = 'white')

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        'Makes a Othello move and redraws the board when tkinter window is clicked.'
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        click_point = point.from_pixel(event.x, event.y, width, height)
        move_click = click_point.pixel(width, height)
        #Determine row
        for row in range(self._game._rows):
            if  row * (height/(self._game._rows)) < move_click[1] and move_click[1] < (row + 1) * (height/(self._game._rows)):
                row_move = row + 1
        #Determine column
        for column in range(self._game._columns):
            if  column * (width/(self._game._columns)) < move_click[0] and move_click[0] < (column + 1) * (width/(self._game._columns)):
                column_move = column + 1
        move = [row_move, column_move]
        try:
            self._game.make_move(move)
            self._draw_board()
        except game_logic.InvalidMoveError:
            pass

###------- PROGRAM START -------###

if __name__ == '__main__':
    game_settings = StartGame()
    game_settings.run()
    OthelloGUI(game_settings).run()
    
###------- PROGRAM END -------###
