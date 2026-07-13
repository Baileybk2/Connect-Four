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

    # Getter methods: only job is to return (give back) information stored inside the object

    def getGrid(self):
        return self._grid

    def getColumnCount(self):
        return self._columns

    # this method is what places the piece and stores the location
    # it will expect 3 things: self= current board, column= column the player chooses, piece= which piece is being dropped
    def placePiece(self, column, piece):
        # error handling for columns not in grid and player selecting EMPTY
        if column < 0 or column is >= self._columns:
            raise ValueError('Invalid Column')
        if piece == GridPosition.EMPTY:
            raise Value Error('Invalid Piece')
        # START, STOP, STEP
        # START: where to begin the loop
        # STOP: stop looping before reaching this value
        # STEP: how much to move each time in the loop
        for row in range(self._rows-1, -1, -1):
            # sets the piece after checking if position the player has chosen is empty
            if self._grid[row][column] == GridPosition.EMPTY
                self._grid[row][column] == piece
                return row

    # this method checks in there is a winning condition
    # it expects self= current board, connectN= the number needed to win, the row, the column, and the piece color
    def checkWin(self, connectN, row, column, piece):
        # starting the count at 0
        count = 0
        # check for horizontal
        # loop through the grid's columns
        for column in range(self._columns):
            # increase the piece's count or remain at 0
            if self._grid[row][column] == piece:
                count += 1
            else:
                count = 0
            # if the count equals connectN, return true for winning condition
            if count == connectN
                return True

        # check for vertical
        # loop through the grid's rows
        count = 0
        for row in range(self._rows):
            # increase the piece's count or remain at 0
            if self._grid[row][column] == piece:
                count += 1
            else:
                count = 0
            # check for winning condition
            if count == connectN
                return True

        # check diagonal
        count = 0
        # currentRow can be written as just r
        # currentColumn can be written as just c
        for r in range(self._rows):
            # currentRow(r) will be the looped element
            # row and column stay constant (the last places the piece was placed)
            # For this diagonal (/), every square has the same value of row + column
            # The line c = row + col - r calculates the correct column for each row so the loop stays on that diagonal
            c = row + column - r
            if c >= 0 or c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN
                return True

        # check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = row - column + r
            if c >= 0 or c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN
                return True

        return False


# player info

class Player:
    def __init__(self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor

    def getName(self):
        return self._name

    def getPieceColor(self):
        return self._pieceColor


# the game class will be used to play the game
# it will keep track of the players, the score, and the grid
class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player('Player 1', GridPosition: YELLOW),
            Player('Player 2', GridPosition: RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0

    def printBoard(self):
        print('Board:/n')
        grid = self._grid.getGrid():
        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GirdPosition.EMPTY:
                    row += '0 '
                elif piece == GrisPosition.YELLOW:
                    row += 'Y '
                elif piece == GridPosition.RED:
                    row += 'R '
            print(row)
        print('')

    def playMove(self, player):
        self.printBoard()
        print(f"{player._getName()}'s turn")
        colCnt = self._grid.getColumnCount()
        moveColumn = int(input(f"Enter a number between {0} and {colCnt - 1} to add piece: "))
        moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
        return (moveRow, moveColumn)

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkWin(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player

    def play(self):
        maxScore = 0
        winner = None
        while maxScore < _self.targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round!")
            maxScore = max(self._score[winner.getName()], maxScore)

            self._grid.initGrid()
        print(f"{winner.getName} won the game!")