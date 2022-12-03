"""Actually create a window and run the game of soduku"""
import pygame, sys
import constants as c
from board import Board
from sudoku_generator import generate_sudoku

def start_screen(screen):
    """Create a game start screen in pygame"""

def run_game(screen, difficulty):
    """Run a game of Soduku"""
    current_list = generate_sudoku(c.GRID_WIDTH, difficulty)
    current_board = Board(c.GRID_WIDTH, c.GRID_WIDTH, screen, difficulty)
    current_board.populate(current_list)
    current_board.draw()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the coordinates of the mouse click
                pos = pygame.mouse.get_pos()
                row_col_pos = Board.click(pos)
                current_board.select(row_col_pos)
                current_board.draw_selection(row_col_pos)
                pygame.display.flip()


                # Prompt the user for a number
                number = input("Enter a number for the cell")

                # Make sure the number is between 1 and 9
                if 1 <= int(number) <= 9:
                    # Update the grid with the new number
                    current_board.sketch(number)

        # Clear the screen
        screen.fill(c.BACK_COLOR)

        current_board.draw()

        # Update the screen
        pygame.display.flip()

def game_over(screen):
    """Create a game over screen in pygame"""
def main():
    """Run to create a pygame Soduku game"""
    pygame.init()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Sudoku")
    start_screen(screen)

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Sudoku")
    run_game(screen, 5)
    #main()
