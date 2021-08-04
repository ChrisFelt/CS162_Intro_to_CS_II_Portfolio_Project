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
        pass

    def set_fence(self, side):
        """Takes a string that corresponds with one of the keys in the self._fence dictionary and sets the value for
        that key to True. Returns nothing."""
        pass

    def set_pawn(self, value):
        """Takes a Boolean and sets self._pawn to that value. Returns nothing."""
        pass

    def get_pawn(self):
        """Takes no parameters and returns self._pawn."""
        pass


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
        pass

    def get_cell(self, coord):
        """Takes a tuple with integer values for column and row as the parameter and returns a Cell object at the
        dictionary location corresponding with coord."""
        pass


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
        pass

    def get_pawn_loc(self):
        """Takes no parameters and returns self._pawn_loc."""
        pass

    def get_fences(self):
        """Takes no parameters and returns self._fences."""
        pass

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
        pass

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
        pass

    def __check_move_legality(self, player, coord):
        """Given an integer that represents the player and a tuple of the coordinate locations of the attempted move,
        determines if the destination cell is on the board. If not, returns False. If it is, then calls the
        orthogonal_move function. If the orthogonal_move function returns True, returns True. If False, calls the
        diagonal_move function. If the diagonal_move function returns True, returns True. Otherwise, this method returns
        False."""
        pass

    def __orthogonal_move(self, player, coord):
        """Given an integer that represents the player and a tuple of the coordinate location of the attempted move,
        first checks if the move is orthogonally adjacent to the current location of the pawn. If it is, checks that
        the opposing player's pawn is not in the destination cell or a fence is in the way - if there aren't, returns
        True. Otherwise checks if destination is 2 spaces away and opposing player's pawn is between the current
        location of the pawn and the destination cell. If they are, checks for fences between the current cell and
        destination cell. If none, returns True. Otherwise, returns False."""
        pass

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
        pass

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
        pass

    def print_board(self):
        """Prints the current state of the Quoridor game board. Used for testing purposes only."""
        pass
