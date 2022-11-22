"""This class represents a single cell in the Sudoku board. There are 81 Cells in a Board."""
import pygame
import constants as c
class Cell(object):
    """Represents a single square on the board"""
    def __init__(self, value, row, col, screen):
        """Constructor for the Cell class"""
    def set_cell_value(self, value):
        """Setter for this cell’s value"""
    def set_sketched_value(self, value):
        """Setter for this cell’s sketched value"""
    def draw(self):
        """Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected."""
