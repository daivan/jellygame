import pygame
import os
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


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


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

            print(block)

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


def main():

    score = 0
    
    board = [
        [0,1,2,3,4,1,4,2,0],
        [0,1,2,3,4,1,4,2,0]
    ]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == RED_HIT:
                red_health -= 1
                #BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                #BULLET_HIT_SOUND.play()

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