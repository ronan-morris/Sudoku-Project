"""This class represents a single cell in the Sudoku board. There are 81 Cells in a Board."""
import pygame
import constants as c
from dataclasses import dataclass

@dataclass
class Cell(object):
    """Represents a single square on the board"""
    value: int
    row: int
    col: int
    width: int
    screen: pygame.Surface


    def __post_init__(self) -> None:
        self.sketched_value = 0
        self.generated = bool(self.value)
        self.center = int(self.width * (self.col + 0.5)), int(self.width * (self.row + 0.5))

    def set_cell_value(self, value) -> None:
        """Setter for this cell’s value"""
        print("set cell value to ",value)
        self.value = value

    def set_sketched_value(self, value) -> None:
        """Setter for this cell’s sketched value"""
        print("set cell sketch value to ",value)
        self.sketched_value = value

    def draw_selection(self) -> None:
        pygame.draw.rect(
            surface = self.screen,
            color = c.SELECTION_COL,
            rect = (
                self.col * c.CELL_PX + 3,
                self.row * c.CELL_PX + 3,
                c.CELL_PX - 5,
                c.CELL_PX - 5
            ),
            width = 2
        )

    def draw(self) -> None:
        """Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected."""
        try:
            given_font = pygame.font.SysFont("Menlo", self.width - 20,bold=True)
            sketch_font = pygame.font.SysFont("Noteworthy", self.width // 2 - 20)
        except OSError:
            given_font = pygame.font.Font(None, self.width - 20)
            sketch_font = pygame.font.Font(None, self.width // 2 - 20)

        pygame.draw.rect(self.screen, c.BACK_COLOR,[
            self.col*self.width +3, self.row*self.width +3,
            self.width -5, self.width -5])

        if self.sketched_value:
            sketch_val_surface = sketch_font.render(str(self.sketched_value), False, c.SKETCHED_VAL_COL, c.BACK_COLOR)
            skew = lambda a : a - self.width * 0.25
            sketch_rect = sketch_val_surface.get_rect(center = (skew(self.center[0]), skew(self.center[1])))
            self.screen.blit(sketch_val_surface, sketch_rect)
        elif self.value:
            given_val_surface = given_font.render(str(self.value), False, c.GIVEN_VAL_COL, c.BACK_COLOR)
            given_rect = given_val_surface.get_rect(center = self.center)
            self.screen.blit(given_val_surface, given_rect)

