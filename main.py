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

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)


HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def draw_window(red, yellow, red_bullets, yellow_bullets, score):
    

    pygame.draw.rect(WIN, BLACK, BORDER)

    score_text = HEALTH_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (10, 760))
    


    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    bajs = pygame.Rect(0, 0, 50, 50)

    pygame.draw.rect(WIN, YELLOW, bajs)

    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    score = 0
    
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

        draw_window(red, yellow, red_bullets, yellow_bullets, score)

    main()


if __name__ == "__main__":
    main()