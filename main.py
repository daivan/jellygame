import pygame
import random
import math

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 450, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jelly Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)

STANDARD_FONT = pygame.font.SysFont('comicsans', 40)

FPS = 60


def draw_window(board, score):

    # clear screen    
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Draw score
    score_text = STANDARD_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (10, 760))
    
    # Draw game board with cubes

    draw_board(board)

    pygame.display.update()


def draw_board(board):
    game_block = pygame.Rect(0, 0, 50, 50)
    pygame.draw.rect(WIN, YELLOW, game_block)

    temp_height = 0
    temp_width = 0
    for row in board:
        temp_width = 0
        for block in row:

            game_block = pygame.Rect(temp_width, temp_height, 50, 50)
            
            if (block == 1):
                color = YELLOW
            elif (block == 2):
                color = BLUE
            elif (block == 3):
                color = RED
            elif (block == 4):
                color = GREEN
            else:
                color = BLACK
            pygame.draw.rect(WIN, color, game_block)

            temp_width = temp_width + 50
        temp_height = temp_height + 50
        #pygame.draw.rect(WIN, YELLOW, bullet)

def draw_winner(text):
    draw_text = STANDARD_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def generate_board():

    board = []
    for x in range(15):
        row = []
        for y in range(9):
            row.append(random.randint(1, 4))
        board.append(row)

    return board

    
def main():

    score = 0
    
    board = generate_board()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('mouse press')
                x, y = pygame.mouse.get_pos()
                column = math.floor(x/50)
                row = math.floor(y/50)
                print(board[row][column])
                board[row][column]=0

        if score > 1000:
            draw_winner('You lost')
            break

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            score = score + 10
            print('A is pressed')

        draw_window(board, score)

    main()


if __name__ == "__main__":
    main()