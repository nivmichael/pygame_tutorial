import pygame
import random

# Init
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Add Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

# Add Enemy
EnemyImg = pygame.image.load('ufo.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_Change = 0


# Player function
def player(x, y):
    screen.blit(playerImg, (x, y))


# Player function
def enemy(x, y):
    screen.blit(EnemyImg, (x, y))


# Game Loop
running = True
while running:
    # RGB - build initial screen
    screen.fill((0, 0, 0))
    # Game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Player Keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change -= 0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change += 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # Change player location on map
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    player(playerX, playerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()
