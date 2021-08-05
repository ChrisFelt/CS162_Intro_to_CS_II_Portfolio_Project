# Author: Christopher Felt
# Date: 8/04/2021
#
# Description: Program for playing a board game called Quoridor.

class Cell:

    """Represents a cell on a Quoridor game board. Holds a dictionary of the four borders of the cell for board edges
    and placement of fences. When the Cell object is created, the initial values for the fences must be passed: None is
    assigned to the edges of the board, and False is assigned to all other borders (a True value means a fence exists
    on that border)."""

    def __init__(self, top, right, bot, left):

        self._fence = {"top": top,      # fence values for the borders of the cell. None = edge of board.
                       "right": right,  # False = no fence. True = fence.
                       "bot": bot,
                       "left": left}

        self._pawn = False  # pawn present in cell

    def get_fence(self, side):
        """Takes a string corresponding with one of the keys in the self._fence dictionary and returns the value for
        that key."""

        return self._fence[side]

    def set_fence(self, side):
        """Takes a string that corresponds with one of the keys in the self._fence dictionary and sets the value for
        that key to True. Returns nothing."""

        self._fence[side] = True

    def set_pawn(self, value):
        """Takes a Boolean and sets self._pawn to that value. Returns nothing."""

        self._pawn = value

    def get_pawn(self):
        """Takes no parameters and returns self._pawn."""

        return self._pawn


class Board:

    """Represents a board for a Quoridor game. Has a compositional relationship with the Cell class; upon creation,
    generates and holds a nested dictionary containing Cell objects for each cell of the board. The board and its
    cells are used by the QuoridorGame class to make moves and place fences."""

    def __init__(self):

        self._cells = {}  # create empty cells dictionary
        self.__generate_cells()  # call generate cells to create the cell dictionary

    def __generate_cells(self):
        """Contains a nested loop: 1 outer loop that iterates through each column and 1 inner loop that iterates
        through each row. Adds a nested dictionary entry to self._cells for each column (key is column number, value is
        a dictionary). The nested dictionary in turn contains the row number as key and a cell object is generated as
        the value. Cell object's fence will be set to None where the edge of the board lies and False for all other cell
        borders."""

        # iterate through columns
        for col in range(9):
            self._cells[col] = {}  # nested empty dictionary with col as key

            # iterate through rows
            for row in range(9):
                # initialize cell borders
                if col == 0:  # set left side of cell
                    left = None  # edge of board
                else:
                    left = False  # no fence, inside of board

                if col == 8:  # set right side of cell
                    right = None
                else:
                    right = False

                if row == 0:  # set top of cell
                    top = None
                else:
                    top = False

                if row == 8:  # set bottom of cell
                    bot = None
                else:
                    bot = False
                # create Cell object as the value for row
                self._cells[col][row] = Cell(top, right, bot, left)

    def get_cell(self, coord):
        """Takes a tuple with integer values for column and row as the parameter and returns a Cell object at the
        dictionary location corresponding with coord."""

        return self._cells[coord[0]][coord[1]]  # return cell object at coord


class Player:

    """Represents a player for the Quoridor game. With an initial ID and pawn location as specified by the initial
    parameters passed. The player also has an initial fences value of 10. The Player class is used by the QuoridorGame
    class to hold and manipulate these values in a single object."""

    def __init__(self, player_id, pawn_loc):
        self._player_id = player_id  # player number (e.g., 1, 2)
        self._pawn_loc = pawn_loc  # cell coordinates of current pawn location
        self._fences = 10  # starting fences

    def set_pawn_loc(self, coord):
        """Takes a tuple with integer values for column and row as the parameter and sets the self._pawn_loc data member
         to it. Returns nothing."""
        self._pawn_loc = coord

    def get_pawn_loc(self):
        """Takes no parameters and returns self._pawn_loc."""
        return self._pawn_loc

    def get_fences(self):
        """Takes no parameters and returns self._fences."""
        return self._fences

    def use_fence(self):
        """Takes no parameters. Reduces self._fences count by 1. Returns nothing."""
        self._fences -= 1


class QuoridorGame:

    """Represents a Quoridor game. Has a compositional relationship with the Player and Board classes; these classes are
    used to store much of the necessary data to play the game. The QuoridorGame calls these classes when it is
    initialized to create a board and two player objects. The game is played through the use of the QuoridorGame methods
    move_pawn and place_fence. Game status can be checked with the is_winner method."""

    def __init__(self):

        self._board = Board()  # generate game board object with Game class
        self._players = {1: Player(1, (4, 0)),
                         2: Player(2, (4, 8))}  # generate dictionary of player objects. pass initial pawn locations.
        self._winner = None  # track game status. can be None, 1, or 2
        self._player_turn = 1  # track turn. player 1 goes first

    def move_pawn(self, player, coord):
        """Given an integer that represents the player and a tuple of the coordinate location of the attempted
        attempted move, first calls the check_initial_parameters method. If False, returns False.
        Otherwise, calls the check_move_legality method. If True, move the pawn by passing
        True to the cell at coord's set_pawn method, clear the previous cell by calling the Player's get_pawn_loc
        method and passing False to the cell at the coord returned, then pass the new coord to the Player's
        set_pawn_loc. Finally, call check_win_condition method by passing the player, change the turn, and return True.
        If check_move_legality returns False, this method returns False."""

        # check game status, values passed, and player turn with check_initial_parameters method
        if self.__check_initial_parameters(player, coord) is False:
            return False  # failed basic checks!

        # check if move is illegal with check_move_legality method
        if self.__check_move_legality(player, coord) is False:
            return False  # illegal move

        else:
            # move pawn to new cell
            self._board.get_cell(coord).set_pawn(True)
            # remove pawn from last cell
            self._board.get_cell(self._players[player].get_pawn_loc()).set_pawn(False)
            # update player's pawn location
            self._players[player].set_pawn_loc(coord)

            # check if this move resulted in a win
            if self.__check_win_condition(player):
                return True  # turn is not changed

            # change the turn
            self.__change_turn()

            return True

    def place_fence(self, player, orient, coord):
        """Given an integer that represents the player, a character (v or h) that represents orientation, and a tuple of
        the coordinate location of the attempted fence placement, first first calls the check_initial_parameters method.
        If False, returns False. Otherwise calls check_fence_legality. If False, returns False. If True, checks if
        orient is "h". If it is, use coords to locate cell in the self._board dictionary and passes "top" to set_fence
        method of the cell. Additionally passes "bot" to the set_fence method of the cell above it, calls the use_fence
        method for the Player, changes player turn, and then returns True. If not "h", checks if orient is "v". If it
        is, use coords to locate cell in the self._board dictionary and passes "left" to set_fence method of the cell.
        Additionally passes "right" to the set_fence method of the cell to the left of it, calls the use_fence method
        for the Player, changes player turn, and then returns True."""
        pass

    def __check_fence_legality(self, orient, coord):
        """Given a character (v or h) that represents orientation, and a tuple of the coordinate location of the
        attempted fence placement, first checks if the current player has 1 or more fences remaining using the
        get_fences method for the Player. If False, returns False. Otherwise, checks if orient is "h". If it is,
        checks if coords are on board AND row is not 0. If True, checks if no fence in place by passing "top" to the
        get_fence method of the cell. If no fence in place, returns True. Otherwise returns False. If not "h", checks if
        orient is "v". If it is, checks if coords are on board AND col is not 0. If True, checks if no fence in place
        by passing "left" to the get_fence method of the cell. If no fence in place, returns True. Otherwise returns
        False."""
        pass

    def is_winner(self, player):
        """Given an integer that represents the player, checks if self._winner is equal to that integer. If it is,
        returns True. Otherwise, returns False."""

        # check if player passed is the winner
        if self._winner == player:
            return True

        else:
            return False

    def __check_move_legality(self, player, coord):
        """Given an integer that represents the player and a tuple of the coordinate locations of the attempted move,
        determines if the opponent's pawn is in the target cell. If it is, returns False. If not, then calls the
        orthogonal_move function. If the orthogonal_move function returns True, returns True. If False, calls the
        diagonal_move function. If the diagonal_move function returns True, returns True. Otherwise, this method returns
        False."""

        # check for opponent's pawn in destination cell
        if self._board.get_cell(coord).get_pawn():
            return False

        # call orthogonal_move function to check if move is orthogonal and no fences block the way
        orthogonal = self.__orthogonal_move(player, coord)
        if orthogonal:
            return True  # move was orthogonal and legal!

        # if move was NOT orthogonal, call diagonal_move to check if move is diagonal and legal
        if orthogonal is None:
            if self.__diagonal_move(player, coord):
                return True  # move was diagonal and legal!

        else:
            return False  # illegal move

    def __orthogonal_move(self, player, coord):
        """Given an integer that represents the player and a tuple of the coordinate location of the attempted move,
        first checks if the move is orthogonally adjacent to the current location of the pawn. If it is, checks that
        the opposing player's pawn is not in the destination cell or a fence is in the way - if there aren't, returns
        True. Otherwise checks if destination is 2 spaces away and opposing player's pawn is between the current
        location of the pawn and the destination cell. If they are, checks for fences between the current cell and
        destination cell. If none, returns True. Otherwise, returns False."""
        pawn_coord = self._players[player].get_pawn_loc()  # current player's pawn coordinates

        # check if direction of move is orthogonal
        if pawn_coord[0] + 1 == coord[0] and pawn_coord[1] == coord[1]:  # moving to right
            if self._board.get_cell(pawn_coord).get_fence("right"):  # check right side of current cell
                return False  # fence in the way!
            else:
                return True  # the way is clear

        if pawn_coord[0] - 1 == coord[0] and pawn_coord[1] == coord[1]:  # moving to left
            if self._board.get_cell(pawn_coord).get_fence("left"):  # check left side of current cell
                return False  # fence in the way!
            else:
                return True  # the way is clear

        if pawn_coord[0] == coord[0] and pawn_coord[1] + 1 == coord[1]:  # moving down
            if self._board.get_cell(pawn_coord).get_fence("bot"):  # check bottom side of current cell
                return False  # fence in the way!
            else:
                return True  # the way is clear

        if pawn_coord[0] == coord[0] and pawn_coord[1] - 1 == coord[1]:  # moving up
            if self._board.get_cell(pawn_coord).get_fence("top"):  # check top side of current cell
                return False  # fence in the way!
            else:
                return True  # the way is clear

        else:
            return None  # not orthogonal (OR fenced in - used only in fair play rule)

    def __diagonal_move(self, player, coord):
        """Given an integer that represents the player and a tuple of the coordinate location of the attempted move,
        first checks if the move is up AND the opposing pawn is up AND a fence is behind the opposing pawn OR the move
        is down AND the opposing pawn is down AND a fence is behind the opposing pawn. Then checks if the move is one to
        the left. If it is, checks the right side of the destination cell if there is a fence. If not, returns True.
        Otherwise, returns False. If the move is not to the left, checks if the move is one to the right. If it is,
        checks the left side of the destination cell if there is a fence. If not, returns True. Otherwise, returns
        False.
        If the opposing pawn is not to the top or bottom of the current player's pawn, checks if it is to the left AND
        move is to the left AND a fence is behind the opposing pawn OR checks if it is to the right AND the move is to
        the right AND a fence is behind the opposing pawn. If true, checks if the move is up one. If it is, checks the
        bottom side of the destination cell for a fence. If none, returns True. If the move is not up, checks if the
        move is down one. If it is, checks the top side of the destination cell if there is a fence. If not, returns
        True. Otherwise, returns False.
        If none of the above, returns False. (Note: if this method becomes too long, it will be split into two parts,
        one for each paragraph above.)"""

        pawn_coord = self._players[player].get_pawn_loc()  # current player's pawn coordinates
        tar_cell = self._board.get_cell(coord)  # destination cell object

        # call diagonal_move_vertical method to check vertical conditions
        if self.__diagonal_move_vertical(coord, pawn_coord, -1, "top") or \
           self.__diagonal_move_vertical(coord, pawn_coord, 1, "bot"):

            # check if move is to the left
            if pawn_coord[0] - 1 == coord[0]:
                if tar_cell.get_fence("right") is False:  # check if fence in the way
                    return True  # move valid!

            # check if move is to the right
            elif pawn_coord[0] + 1 == coord[0]:
                if tar_cell.get_fence("left") is False:  # check if fence in the way
                    return True  # move valid!

            else:
                return False  # illegal move

        # call diagonal_move_vertical method to check horizontal conditions
        if self.__diagonal_move_horizontal(coord, pawn_coord, -1, "left") or \
           self.__diagonal_move_horizontal(coord, pawn_coord, 1, "right"):

            # check if move is up
            if pawn_coord[1] - 1 == coord[1]:
                if tar_cell.get_fence("bot") is False:  # check if fence in the way
                    return True  # move valid!

            # check if move is down
            elif pawn_coord[1] + 1 == coord[1]:
                if tar_cell.get_fence("top") is False:  # check if fence in the way
                    return True  # move valid!

            else:
                return False  # illegal move

    def __diagonal_move_vertical(self, coord, pawn_coord, value, side):
        """Given a tuple of two integers representing coordinates, the coordinates of the current player's pawn,
        an integer value 1 or -1, and a string that corresponds with a cell side, saves the following checks as
        Booleans:
        1. Destination cell is up or down
        2. Opposing pawn is adjacent and orthogonally up or down with respect to current player's pawn
        3. No fences obstruct movement to destination cell.
        Returns True if all of these conditions are True. Otherwise, returns False"""

        # check if move is up or down
        direc = pawn_coord[1] + value == coord[1]
        # check if opposing pawn orthogonally up or down and adjacent
        pawn = self._board.get_cell((coord[0], coord[1] + value)).get_pawn()
        # check if fence behind opposing pawn
        fence =  self._board.get_cell((coord[0], coord[1] + value)).get_fence(side)

        return direc and pawn and fence

    def __diagonal_move_horizontal(self, coord, pawn_coord, value, side):
        """Given a tuple of two integers representing coordinates, the coordinates of the current player's pawn,
        an integer value 1 or -1, and a string that corresponds with a cell side, saves the following checks as
        Booleans:
        1. Destination cell is left or right
        2. Opposing pawn is adjacent and orthogonally left or right with respect to current player's pawn
        3. No fences obstruct movement to destination cell.
        Returns True if all of these conditions are True. Otherwise, returns False"""

        # check if move is left or right
        direc = pawn_coord[0] + value == coord[0]
        # check if opposing pawn orthogonally left or right and adjacent
        pawn = self._board.get_cell((coord[0] + value, coord[1])).get_pawn()
        # check if fence behind opposing pawn
        fence =  self._board.get_cell((coord[0] + value, coord[1])).get_fence(side)

        return direc and pawn and fence

    def __check_win_condition(self, player):
        """Given an integer that represents the player, if player 1, checks if their pawn location is on row 8. If it
        is, sets self._winner to 1 and returns True. If player 2, checks if their pawn location is on row 0. If it
        is, sets self._winner to 2 and returns True. Otherwise returns False."""
        pass

    def __check_initial_parameters(self, player, coord, orient=None):
        """Given an integer that represents the player, a tuple of the coordinate location of the attempted fence
        placement, and a character (v or h) that represents orientation (optional; default is None), first checks if the
        game has been won. If it has, returns False. If not, checks if it's the player's turn. If not, returns False.
        Otherwise checks if coord is a tuple with two integers and is on the board. If not, returns False. Then, if
        orient is not None, checks if orient is a character and is "v" or "h". If not, returns False. Otherwise, returns
        true."""
        # check game status
        if self._winner is not None:
            return False  # game is over!

        # check if it's the player's turn
        if self._player_turn != player:
            return False

        # check if coord is a tuple and contains two integers
        if type(coord) is tuple and type(coord[0]) is int and type(coord[1]) is int:
            if coord[0] not in range(9) or coord[1] not in range(9):  # check if coord is inside board
                return False  # out of bounds!
        else:
            return False  # unexpected value passed!

        # check if orient variable passed
        if orient is not None:
            if orient != 'v' or orient != 'h':  # check if v or h passed
                return False  # unexpected value!

        return True

    def __change_turn(self):
        """Takes no parameters. Changes the turn to the next player. Returns nothing."""
        # change to second player's turn if currently player one's turn
        if self._player_turn == 1:
            self._player_turn = 2

        # change to first player's turn if currently player two's turn
        else:
            self._player_turn = 1

    def print_board(self):
        """Prints the current state of the Quoridor game board. Used for testing purposes only."""

        for col in range(9):  # iterate through cols

            for row in range(9):  # iterate through rows

                print(str(col)+str(row), " ", end='')  # print cell coords in line

                if self._board.get_cell((col, row)).get_side("top"):
                    print("t", end='')  # print top fence in line

                if self._board.get_cell((col, row)).get_side("right"):
                    print("r", end='')  # print right fence in line

                if self._board.get_cell((col, row)).get_side("bot"):
                    print("b", end='')  # print bottom fence in line

                if self._board.get_cell((col, row)).get_side("left"):
                    print("l", end='')  # print left fence in line

                if self._board.get_cell((col, row)).get_pawn():
                    print("P", end='')  # print pawne in line

            print("\n")  # new line after each row
