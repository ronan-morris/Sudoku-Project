"""This class represents an entire Sudoku board. A Board object has 81 Cell objects"""
import pygame
import constants as c
from cell import Cell
from dataclasses import dataclass
from sudoku_generator import SudokuGenerator

@dataclass
class Board(object):
    """Represents the 9x9 board of cell objects"""

    """Construct a Board object.
    screen is a window from PyGame.
    difficulty is a variable to indicate if the user chose easy, medium, or hard."""
    width: int
    height: int
    screen: pygame.Surface
    difficulty: int
    def __post_init__(self) -> None:
        self.table = []

    def populate(self, sudoku_ls) -> None:
        for i, row in enumerate(sudoku_ls):
            table_row = []
            for j, val in enumerate(row):
                table_row.append(Cell(val, i, j, c.CELL_PX, self.screen))
            self.table.append(table_row)

    def draw(self) -> None:
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board."""
        for row in self.table:
            map(Cell.draw, row)
        for i in range(c.GRID_WIDTH + 1):
            pygame.draw.line(
                surface = self.screen,
                color = c.LINE_COL,
                start_pos = (i * c.CELL_PX,0),
                end_pos = (i * c.CELL_PX, c.HEIGHT),
                width = 1 + int(i % c.BOX_WIDTH == 0))
            pygame.draw.line(
                surface = self.screen,
                color = c.LINE_COL,
                start_pos = (0, i * c.CELL_PX),
                end_pos = (c.HEIGHT, i * c.CELL_PX),
                width = 1 + int(i % c.BOX_WIDTH == 0))
    def select(self, row, col) -> None:
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""
        self.selected = self.table[row][col]

    @staticmethod
    def click(x, y):
        """If a tuple of (x,y) coordinates is within the displayed board, this function returns a tuple of the (row,col)
        of the cell which was clicked. Otherwise, this function returns None."""
        if y < c.HEIGHT:
            return x // c.CELL_PX, y // c.CELL_PX
        else:
            return None

    def clear(self) -> None:
        """Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves."""
        if not self.selected.generated:
            self.selected.set_cell_value(0)
            self.selected.set_sketched_value(0)

    def sketch(self, value) -> None:
        """Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function."""
        if not self.selected.generated:
            self.selected.set_sketched_value(value)
            self.selected.draw()

    def place_number(self) -> None:
        """Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key."""
        self.selected.set_cell_value(self.selected.sketched_value)
        self.selected.set_sketched_value(0)
        self.selected.draw()

    def reset_to_original(self) -> None:
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)."""
        for row in self.table:
            for cell in row:
                if not cell.generated:
                    cell.set_sketched_value(0)
                    cell.set_cell_value(0)

    def is_full(self) -> bool:
        """Returns a Boolean value indicating whether the board is full or not."""
        return not self.find_empty()

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""
        for i, row in enumerate(self.table):
            for j, cell in enumerate(row):
                if not cell.value:
                    return i , j
        return False

    def check_board(self) ->bool:
        """Check whether the Sudoku board is solved correctly."""
        ls_1_9 = range(c.GRID_WIDTH)[1:]
        for row in self.table:
            if sorted([cell.value for cell in row]) != ls_1_9:
                return False
        for i in range(len(self.table)):
            if sorted([ row[i].value for row in self.table ]) != ls_1_9:
                return False
            box = [row[i/ c.GRID_WIDTH : i//c.GRID_WIDTH +3] for row in self.table[i%c.GRID_WIDTH : i%c.GRID_WIDTH +3]]
            if sorted([ cell.value for cell in sum(box, []) ]) != ls_1_9:
                return False
        return True

