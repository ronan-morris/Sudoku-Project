"""Actually create a window and run the game of soduku"""
import pygame, sys
import constants as c
from board import Board
from sudoku_generator import generate_sudoku

def start_screen(screen):
    """Create a game start screen in pygame"""
    imp = pygame.image.load('FinalHomeScreen.jpeg').convert()
    screen.blit(imp, (0, 0))
    mouse = pygame.mouse.get_pos()
    width = screen.get_width() 
    height = screen.get_height()
    color1 = (255,255,255)
    color2 = (0,0,0)
    color_light = (170,170,170)
    color_dark = (100,100,100) 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2-300,height/2+200,140,40]) 
        pygame.draw.rect(screen,color_light,[width/2,height/2+200,140,40])
        pygame.draw.rect(screen,color_light,[width/2+300,height/2+200,140,40]) 
    else: 
        pygame.draw.rect(screen,color_dark,[width/2-300,height/2+200,140,40])
        pygame.draw.rect(screen,color_dark,[width/2,height/2+200,140,40])
        pygame.draw.rect(screen,color_dark,[width/2+300,height/2+200,140,40])
    font = pygame.font.SysFont('Comic Sans', 36)
    easy = font.render('Easy', True, color1)
    medium = font.render('Medium', True, color1)
    hard = font.render('Hard', True, color1)
    screen.blit(easy, (width/2-300,height/2+200)) 
    screen.blit(medium, (width/2,height/2+200)) 
    screen.blit(hard, (width/2+300,height/2+200)) 
    pygame.display.flip()
    while True:
        pass

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
    start_screen(screen)
    pygame.display.set_caption("Sudoku")

if __name__ == "__main__":
    main()
