### CONSTANTS ###

NONE = 0
BLACK = 1
WHITE = 2

### CLASSES ###

class InvalidMoveError(Exception):
    'Raised whenever an invalid move is made'
    pass


class Othello:
    def __init__(self, rows: int,
                 columns: int,
                 first_turn: int,
                 arrangement: int, 
                 how_to_win: str):
        self._rows = rows
        self._columns = columns
        self._turn = first_turn
        self._arrangement = arrangement
        self._how_to_win = how_to_win
        self._game_state = self._new_game()
              
### PUBLIC METHODS ###

    def count_discs(self) -> [int,int]:
        'Counts number of black and number of white pieces and returns a list of counts.'
        count_list = []
        total_black = 0
        total_white = 0
        for lst in self._game_state:
            total_black += lst.count(BLACK)
            total_white += lst.count(WHITE)
        count_list.append(total_black)
        count_list.append(total_white)
        return count_list

    def game_over(self) -> bool:
        'Returns True if game is over'
        game_over = False
        none_in_game = []
        for row in self._game_state:
            if NONE in row:
                none_in_game.append(True)
            else:
                none_in_game.append(False)
        if True not in none_in_game:
            game_over = True
        check_valid_moves_on_board = self._check_valid_moves_on_board()
        if check_valid_moves_on_board == False:
            game_over = True
        return game_over

    def winner(self) -> 'winner':
        'Returns the winner of the game.'
        winner = NONE
        total_black = 0
        total_white = 0
        for lst in self._game_state:
            total_black += lst.count(BLACK)
            total_white += lst.count(WHITE)
        if self._how_to_win == '>':
            if total_black > total_white:
                winner = BLACK
            elif total_white > total_black:
                winner = WHITE
        elif self._how_to_win == '<':
            if total_black > total_white:
                winner = WHITE
            elif total_white > total_black:
                winner = BLACK
        return winner

    def make_move(self, move: list) -> None:
        'Checks that move is valid, then makes move by placing disc and flipping appropriate discs.'
        self._out_of_bounds(move)
        self._check_move_valid(move)
        row = move[0]-1
        column = move[1]-1
        if self._check_move_valid(move) == False:
            raise InvalidMoveError()
        elif self._check_move_valid(move) == True:
            #drops disc
            if self._turn == BLACK:
                self._game_state[move[0]-1][move[1]-1] = BLACK
            else:
                self._game_state[move[0]-1][move[1]-1] = WHITE
            #flips opposing discs - horizontal
            if (column - 1) >= 0:
                if self._game_state[row][column - 1] == self._opposite_turn():
                    count = 1
                    column -= 1
                    while (column - 1) >= 0:
                        if self._game_state[row][column - 1] == self._opposite_turn():
                            column -= 1
                            count += 1
                            pass
                        elif self._game_state[row][column - 1] == self._turn:
                            for i in range(count):
                                self._game_state[row][(column - 1) + 1] = self._turn
                                column += 1
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (column + 1) <= self._columns - 1:
                if self._game_state[row][column + 1] == self._opposite_turn():
                    count = 1
                    column += 1
                    while (column + 1) <= self._columns - 1:
                        if self._game_state[row][column + 1] == self._opposite_turn():
                            column += 1
                            count += 1
                            pass
                        elif self._game_state[row][column + 1] == self._turn:
                            for i in range(count):
                                self._game_state[row][(column + 1) - 1] = self._turn
                                column -= 1
                            break
                        else:
                            break
            #flips opposing discs - vertical
            row = move[0]-1
            column = move[1]-1
            if (row - 1) >= 0:
                if self._game_state[row - 1][column] == self._opposite_turn():
                    count = 1
                    row -= 1
                    while (row - 1) >= 0:
                        if self._game_state[row - 1][column] == self._opposite_turn():
                            row -= 1
                            count += 1
                            pass
                        elif self._game_state[row - 1][column] == self._turn:
                            for i in range(count):
                                self._game_state[(row - 1) + 1][column] = self._turn
                                row += 1
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row + 1) <= self._rows - 1:
                if self._game_state[row + 1][column] == self._opposite_turn():
                    count = 1
                    row += 1
                    while (row + 1) <= self._rows - 1:
                        if self._game_state[row + 1][column] == self._opposite_turn():
                            row += 1
                            count += 1
                            pass
                        elif self._game_state[row + 1][column] == self._turn:
                            for i in range(count):
                                self._game_state[(row + 1) - 1][column] = self._turn
                                row -= 1
                            break
                        else:
                            break
            #flips opposing discs - diagonal
            row = move[0]-1
            column = move[1]-1
            if (row - 1) >= 0 and (column - 1) >= 0:
                if self._game_state[row - 1][column - 1] == self._opposite_turn():
                    count = 1
                    row -= 1
                    column -= 1
                    while (row - 1) >= 0 and(column - 1) >= 0:
                        if self._game_state[row - 1][column - 1] == self._opposite_turn():
                            row -= 1
                            column -= 1
                            count += 1
                            pass
                        elif self._game_state[row - 1][column - 1] == self._turn:
                            for i in range(count):
                                self._game_state[(row - 1) + 1][(column - 1) + 1] = self._turn
                                row += 1
                                column += 1
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row + 1) <= self._rows - 1 and (column - 1) >= 0:
                if self._game_state[row + 1][column - 1] == self._opposite_turn():
                    count = 1
                    row += 1
                    column -= 1
                    while (row + 1) <= self._rows - 1 and(column - 1) >= 0:
                        if self._game_state[row + 1][column - 1] == self._opposite_turn():
                            row += 1
                            column -= 1
                            count += 1
                            pass
                        elif self._game_state[row + 1][column - 1] == self._turn:
                            for i in range(count):
                                self._game_state[(row + 1) - 1][(column - 1) + 1] = self._turn
                                row -= 1
                                column += 1
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row - 1) >= 0 and (column + 1) <= self._columns - 1:
                if self._game_state[row - 1][column + 1] == self._opposite_turn():
                    count = 1
                    row -= 1
                    column += 1
                    while (row - 1) >= 0 and (column + 1) <= self._columns - 1:
                        if self._game_state[row - 1][column + 1] == self._opposite_turn():
                            row -= 1
                            column += 1
                            count += 1
                            pass
                        elif self._game_state[row - 1][column + 1] == self._turn:
                            for i in range(count):
                                self._game_state[(row - 1) + 1][(column + 1) - 1] = self._turn
                                row += 1
                                column -= 1
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row + 1) <= self._rows - 1 and (column + 1) <= self._columns - 1:
                if self._game_state[row + 1][column + 1] == self._opposite_turn():
                    count = 1
                    row += 1
                    column += 1
                    while (row + 1) <= self._rows - 1 and (column + 1) <= self._columns - 1:
                        if self._game_state[row + 1][column + 1] == self._opposite_turn():
                            row += 1
                            column += 1
                            count += 1
                            pass
                        elif self._game_state[row + 1][column + 1] == self._turn:
                            for i in range(count):
                                self._game_state[(row + 1) - 1][(column + 1) - 1] = self._turn
                                row -= 1
                                column -= 1
                            break
                        else:
                            break
        self._change_turn()


### PRIVATE METHOD ###
        
    def _new_game(self) -> [[int]]:
        'Returns a new game with the arrangement determined.'
        board = self._new_board()
        if self._arrangement == BLACK:
            board[int((self._rows/2)-1)][int((self._columns/2)-1)] = BLACK
            board[int((self._rows/2)-1)][int(self._columns/2)] = WHITE
            board[int(self._rows/2)][int((self._columns/2)-1)] = WHITE
            board[int(self._rows/2)][int(self._columns/2)] = BLACK
        else:
            board[int((self._rows/2)-1)][int((self._columns/2)-1)] = WHITE
            board[int((self._rows/2)-1)][int(self._columns/2)] = BLACK
            board[int(self._rows/2)][int((self._columns/2)-1)] = BLACK
            board[int(self._rows/2)][int(self._columns/2)] = WHITE
        return board

    def _new_board(self) -> [[int]]:
        'Creates a new game board with the rows and column size determined.'
        board = []
        for row in range(self._rows):
            board.append([])
        for sublist in board:
            for columns in range(self._columns):
                sublist.append(NONE)
        return board
        
    def _check_move_valid(self, move:list) -> bool:
        'Checks if the move is valid, only returns bool if the move is valid.'
        valid_move = False
        end_piece = False
        opposite_pieces = False
        row = move[0]-1
        column = move[1]-1
        if self._game_state[row][column] == NONE:    
            #check horizontal
            if (column - 1) >= 0:
                if self._game_state[row][column - 1] == self._opposite_turn():
                    column -= 1
                    while (column - 1) >= 0:
                        if self._game_state[row][column - 1] == self._opposite_turn():
                            column -= 1
                            pass
                        elif self._game_state[row][column - 1] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (column + 1) <= self._columns - 1:
                if self._game_state[row][column + 1] == self._opposite_turn():
                    column += 1
                    while (column + 1) <= self._columns - 1:
                        if self._game_state[row][column + 1] == self._opposite_turn():
                            column += 1
                            pass
                        elif self._game_state[row][column + 1] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            #checks vertical
            row = move[0]-1
            column = move[1]-1
            if (row - 1) >= 0:
                if self._game_state[row - 1][column] == self._opposite_turn():
                    row -= 1
                    while (row - 1) >= 0:
                        if self._game_state[row - 1][column] == self._opposite_turn():
                            row -= 1
                            pass
                        elif self._game_state[row - 1][column] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row + 1) <= self._rows - 1:
                if self._game_state[row + 1][column] == self._opposite_turn():
                    row += 1
                    while (row + 1) <= self._rows - 1:
                        if self._game_state[row + 1][column] == self._opposite_turn():
                            row += 1
                            pass
                        elif self._game_state[row + 1][column] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            #checks diagonal
            row = move[0]-1
            column = move[1]-1
            if (row - 1) >= 0 and (column - 1) >= 0:
                if self._game_state[row - 1][column - 1] == self._opposite_turn():
                    row -= 1
                    column -= 1
                    while (row - 1) >= 0 and(column - 1) >= 0:
                        if self._game_state[row - 1][column - 1] == self._opposite_turn():
                            row -= 1
                            column -= 1
                            pass
                        elif self._game_state[row - 1][column - 1] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row + 1) <= self._rows - 1 and (column - 1) >= 0:
                if self._game_state[row + 1][column - 1] == self._opposite_turn():
                    row += 1
                    column -= 1
                    while (row + 1) <= self._rows - 1 and(column - 1) >= 0:
                        if self._game_state[row + 1][column - 1] == self._opposite_turn():
                            row += 1
                            column -= 1
                            pass
                        elif self._game_state[row + 1][column - 1] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row - 1) >= 0 and (column + 1) <= self._columns - 1:
                if self._game_state[row - 1][column + 1] == self._opposite_turn():
                    row -= 1
                    column += 1
                    while (row - 1) >= 0 and (column + 1) <= self._columns - 1:
                        if self._game_state[row - 1][column + 1] == self._opposite_turn():
                            row -= 1
                            column += 1
                            pass
                        elif self._game_state[row - 1][column + 1] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
            row = move[0]-1
            column = move[1]-1
            if (row + 1) <= self._rows - 1 and (column + 1) <= self._columns - 1:
                if self._game_state[row + 1][column + 1] == self._opposite_turn():
                    row += 1
                    column += 1
                    while (row + 1) <= self._rows - 1 and (column + 1) <= self._columns - 1:
                        if self._game_state[row + 1][column + 1] == self._opposite_turn():
                            row += 1
                            column += 1
                            pass
                        elif self._game_state[row + 1][column + 1] == self._turn:
                            end_piece = True
                            opposite_pieces = True
                            break
                        else:
                            break
        if end_piece == False and opposite_pieces == False:
            valid_move = False
        else:
            valid_move = True
        return valid_move

    def _check_valid_moves_on_board(self)-> bool:
        'Checks if there are valid moves on the board, returns True if there is.'
        valid_moves_on_board = True
        all_moves_available = []
        valid_move = []
        for i in range(len(self._game_state)):
            for j in range(len(self._game_state[i])):
                if self._game_state[i][j] == NONE:
                   all_moves_available.append([i+1, j+1])     
        for move in all_moves_available:
            valid = self._check_move_valid(move)
            valid_move.append(valid)
        if True not in valid_move:
            self._change_turn()
            all_moves_available = []
            valid_move = []
            for i in range(len(self._game_state)):
                for j in range(len(self._game_state[i])):
                    if self._game_state[i][j] == NONE:
                       all_moves_available.append([i+1, j+1])     
            for move in all_moves_available:
                valid = self._check_move_valid(move)
                valid_move.append(valid)
            if True not in valid_move:
                valid_moves_on_board = False
                return valid_moves_on_board
        return valid_moves_on_board

    def _opposite_turn(self) -> "opposite turn":
        'Returns the opposite turn.'
        if self._turn == BLACK:
            return WHITE
        else:
            return BLACK
    
    def _change_turn(self) -> None:
        'Given the player whose turn it is now, change the turn to the opposite player.'
        if self._turn == BLACK:
            self._turn = WHITE
        else:
            self._turn = BLACK
        
    def _out_of_bounds(self, move: []) -> None:
        'Raises an InvalidMoveError if row and column are out of bounds of the board'
        if move[0] > len(self._game_state):
            raise InvalidMoveError()
        elif move[0] <= 0:
            raise InvalidMoveError()
        elif move[1] > len(self._game_state[0]):
            raise InvalidMoveError()
        elif move[1] <= 0:
            raise InvalidMoveError()
