# An Automated game similar to dino game logic which is automated
import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
GROUND_HEIGHT = 50
FPS = 55

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

dino_rect = pygame.Rect(100, HEIGHT - GROUND_HEIGHT - 25, 50, 50)
dino_x_speed = 5
dino_y_speed = 0

cactus_rect = pygame.Rect(WIDTH + 20, HEIGHT - GROUND_HEIGHT - 25, 20, 50)
cactus_x_speed = -5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino game(sorta)")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if dino_rect.bottom == HEIGHT - GROUND_HEIGHT:
        dino_y_speed = -15

    dino_rect.x += dino_x_speed
    dino_rect.y += dino_y_speed

    if dino_rect.right > WIDTH - 50:
        dino_rect.right = WIDTH - 50
        dino_x_speed = -5
    elif dino_rect.left < 0:
        dino_rect.left = 0
        dino_x_speed = 5

    if dino_rect.bottom < HEIGHT - GROUND_HEIGHT:
        dino_y_speed += 1
    elif dino_rect.bottom > HEIGHT - GROUND_HEIGHT:
        dino_rect.bottom = HEIGHT - GROUND_HEIGHT
        dino_y_speed = 0

    cactus_rect.x += cactus_x_speed

    if cactus_rect.right < 0:
        cactus_rect.left = WIDTH + random.randint(100, 300)
        cactus_rect.bottom = HEIGHT - GROUND_HEIGHT - 25

    if dino_rect.colliderect(cactus_rect):
        print("You hit an obstacle -__-!")

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, dino_rect)
    pygame.draw.rect(screen, RED, cactus_rect)

    pygame.draw.rect(screen, BLACK, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
