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

def game_over(screen):
    """Create a game over screen in pygame"""
def main():
    """Run to create a pygame Soduku game"""
    pygame.init()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Sudoku")
    start_screen(screen)

if __name__ == "__main__":
    main()
