"""Actually create a window and run the game of soduku"""
import pygame, sys
import constants as c
from board import Board
from sudoku_generator import generate_sudoku

def start_screen(screen):
    """Create a game start screen in pygame"""
    try:
        imp = pygame.image.load('FinalHomeScreen.jpeg').convert()
        screen.blit(imp, (0, 0))
    except FileNotFoundError:
        screen.fill(c.BACK_COLOR)
    button_font = pygame.font.SysFont('Georgia', 36)
    done = False
    while not done:
        mouse = pygame.mouse.get_pos()
        selected_button = 0
        if c.HEIGHT//2 + 2 * c.CELL_PX <= mouse[1] <= c.HEIGHT//2 + 2 * c.CELL_PX + 40:
            for i in range(3):
                button_x_coord = c.WIDTH/2 + (i-1) * c.BOX_WIDTH * c.CELL_PX
                if button_x_coord <= mouse[0] <= button_x_coord + 140:
                    selected_button = i + 1
        for i, difficulty_txt in enumerate(['Easy', 'Medium', 'Hard']):
            if selected_button == i + 1:
                button_col = c.HOVERED_BUTTON_COL
            else:
                button_col = c.NORMAL_BUTTON_COL
            button_x_coord = c.WIDTH//2 + (i-1) * c.BOX_WIDTH * c.CELL_PX
            pygame.draw.rect(screen, button_col, [button_x_coord, c.HEIGHT//2 + 2 * c.CELL_PX , 140, 40])
            current_button = button_font.render(difficulty_txt, True, c.BUTTON_TEXT_COL)
            screen.blit(current_button, (button_x_coord, c.HEIGHT//2 + 2 * c.CELL_PX))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN and selected_button:
                run_game(screen, selected_button * 10 + 20)

        pygame.display.flip()

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
    main()
