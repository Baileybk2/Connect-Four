print("Welcome to Connect Four")

# use an enum to represent the GridPosition
import enum

# Think of a class like a blueprint.
# Just like a blueprint for a house doesn't build a house by itself, this class doesn't create a game board yet
# It simply describes what every Grid object should have.

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

# the grid class with maintain the state of the board and of all of the pieces
class Grid:
    # the constructor
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        # right now we don't have a board yet, we will make it later
        self._grid = None
        # function for building the grid with EMPTY value from enum above
        # runs each time the Grid is created
        self.initGrid()

    def initGrid(self):
        # for however many rows and columns to loop through, EMPTY is inserted into each one
        self._grid = [[GridPosition.EMPTY for _ in range(self._columns)] for _ in range(self._rows)]


