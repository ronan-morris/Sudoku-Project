"""Actually create a window and run the game of soduku"""
import pygame, sys
import constants as c
from board import Board
from sudoku_generator import generate_sudoku

def get_button_x(i) -> int:
    return c.WIDTH/2 + (i-1) * c.BOX_WIDTH * c.CELL_PX - 70

def start_screen(screen):
    """Create a game start screen in pygame"""
    try:
        imp = pygame.image.load('FinalHomeScreen.jpeg').convert()
        imp = pygame.transform.scale(imp, (c.WIDTH, c.HEIGHT))
        screen.blit(imp, (0, 0))
    except FileNotFoundError:
        screen.fill(c.BACK_COLOR)
    done = False
    while not done:
        mouse = pygame.mouse.get_pos()
        selected_button = 0
        if c.HEIGHT//2 + 2 * c.CELL_PX <= mouse[1] <= c.HEIGHT//2 + c.CELL_PX * 3:
            for i in range(3):
                button_x_coord = get_button_x(i)
                if button_x_coord <= mouse[0] <= button_x_coord + 140:
                    selected_button = i + 1
        for i, difficulty_txt in enumerate(['Easy', 'Medium', 'Hard']):
            if selected_button == i + 1:
                button_col = c.HOVERED_BUTTON_COL
            else:
                button_col = c.NORMAL_BUTTON_COL
            button_x_coord = get_button_x(i)
            pygame.draw.rect(screen, button_col, [button_x_coord, c.HEIGHT//2 + 2 * c.CELL_PX , 140, c.CELL_PX // 2])
            current_button = button_font.render(difficulty_txt, True, c.BUTTON_TEXT_COL)
            screen.blit(current_button, (button_x_coord, c.HEIGHT//2 + 2 * c.CELL_PX))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN and selected_button:
                run_game(screen, selected_button * 10 + 20)
                done = True

        pygame.display.flip()

def run_game(screen, difficulty):
    """Run a game of Soduku"""
    current_list = generate_sudoku(c.GRID_WIDTH, difficulty)
    current_board = Board(c.GRID_WIDTH, c.GRID_WIDTH, screen, difficulty)
    current_board.populate(current_list)

    screen.fill(c.BACK_COLOR)
    current_board.draw()

    done = False
    buttons_not_drawn = True
    row_col_pos = [0,0]
    while not done:

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            #screen.fill(c.BACK_COLOR)
            current_board.draw()

            if event.type == pygame.QUIT:
                done = True

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the coordinates of the mouse click
                if Board.click(pos):
                    row_col_pos = list(Board.click(pos))
                    current_board.select(row_col_pos)
                elif get_button_x(0) < pos[0] < get_button_x(0) + 140:
                    current_board.reset_to_original()
                elif get_button_x(1) < pos[0] < get_button_x(1) + 140:
                    start_screen(screen)
                    done = True
                elif get_button_x(2) < pos[0] < get_button_x(2) + 140:
                    done = True

            if event.type == pygame.KEYDOWN:
                print(event.__dict__)
                key = event.__dict__['key']
                if key == 13:
                    print("got keypress, trying to place number")
                    current_board.place_number()
                    if current_board.is_full():
                        game_over(screen, current_board.check_board())
                elif 49 <= key <= 57:
                    current_board.sketch(int(key - 48))
                elif 1073741903 <= key <= 1073741906:
                    key -= 1073741903
                    row_col_pos[1 - key // 2] += 1 - (key % 2) * 2
                    print(row_col_pos)
                    try:
                        current_board.select(row_col_pos)
                    except IndexError:
                        row_col_pos[1 - key // 2] -= 1 - (key % 2) * 2

                #escape is 27 if we want that to do something

        if pos[1] > c.WIDTH - 20 or buttons_not_drawn:
            buttons_not_drawn = False
            for i, fn_txt in enumerate(['Reset', 'Restart', 'Exit']):
                button_x_coord = get_button_x(i)
                if button_x_coord <= pos[0] <= button_x_coord + 140 and pos[1] > c.WIDTH :
                    button_col = c.HOVERED_BUTTON_COL
                else:
                    button_col = c.NORMAL_BUTTON_COL
                pygame.draw.rect(screen, button_col, [button_x_coord, int(c.HEIGHT * .925), 140, c.CELL_PX // 2])
                current_button = button_font.render(fn_txt, True, c.BUTTON_TEXT_COL)
                screen.blit(current_button, (button_x_coord, int(c.HEIGHT * .925)))

        # Update the screen
        pygame.display.flip()

def game_over(screen, winstate):
    """Create a game over screen in pygame"""
def main():
    """Run to create a pygame Soduku game"""
    pygame.init()
    global button_font
    button_font = pygame.font.SysFont(c.BUTTON_FONT_NAME, c.CELL_PX // 3)
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Sudoku")
    start_screen(screen)

if __name__ == "__main__":
    main()
