board = [
    0,
    0,
    4,
    0,
    5,
    0,
    0,
    0,
    0,
    9,
    0,
    0,
    7,
    3,
    4,
    6,
    0,
    0,
    0,
    0,
    3,
    0,
    2,
    1,
    0,
    4,
    9,
    0,
    3,
    5,
    0,
    9,
    0,
    4,
    8,
    0,
    0,
    9,
    0,
    0,
    0,
    0,
    0,
    3,
    0,
    0,
    7,
    6,
    0,
    1,
    0,
    9,
    2,
    0,
    3,
    1,
    0,
    9,
    7,
    0,
    2,
    0,
    0,
    0,
    0,
    9,
    1,
    8,
    2,
    0,
    0,
    3,
    0,
    0,
    0,
    0,
    6,
    0,
    1,
    0,
    0,
]


class Grid:
    def __init__(self, board):
        self.board = board
        self.rowSize = 9

    # Display the grid as a sudoku board
    def __str__(self):
        string = ""
        for i in range(self.rowSize):
            for j in range(self.rowSize):
                string += str(self.getSquareValue(i, j)) + " "
            string += "\n"
        return string

    # Return a row of the grid
    def getRow(self, row):
        return self.board[self.getSquareIndex(row, 0) : self.getSquareIndex(row, self.rowSize)]

    # Return a column of the grid
    def getColumn(self, column):
        return self.board[column :: self.rowSize]

    # Return a 3x3 square of the grid
    def getSquare(self, row, column):
        square = []
        for i in range(3):
            for j in range(3):
                square.append(self.board[(row * 3 + i) * self.rowSize + (column * 3 + j)])
        return square

    # Get the index of a square in the grid
    def getSquareIndex(self, row, column):
        return row * self.rowSize + column

    # Get the value of a square in the grid
    def getSquareValue(self, row, column):
        return self.board[self.getSquareIndex(row, column)]

    # Set the value of a square in the grid
    def setSquareValue(self, row, column, value):
        self.board[self.getSquareIndex(row, column)] = value

    # Check if a value is valid for a square in the grid
    def isValid(self, row, column, value):
        # Is the value on the row?
        if value in self.getRow(row):
            return False
        # Is the value on the column?
        if value in self.getColumn(column):
            return False
        # Is the value in the square?
        if value in self.getSquare(row // 3, column // 3):
            return False
        # If the value is not on the row, column or square, it is valid
        return True

    # Get a list of all the values for a square in the grid
    def getValues(self, row, column):
        values = []
        for i in range(1, 10):
            if self.isValid(row, column, i):
                values.append(i)
        return values

    def solve(self):
        for i in range(self.rowSize):
            for j in range(self.rowSize):
                if self.getSquareValue(i, j) == 0:
                    for value in self.getValues(i, j):
                        self.setSquareValue(i, j, value)
                        self.solve()
                        self.setSquareValue(i, j, 0)
                    return
        print(self)


grid = Grid(board)
print(grid)
grid.solve()
