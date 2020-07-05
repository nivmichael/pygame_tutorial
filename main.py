import pygame
import random

# Init
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background Image
background = pygame.image.load('background.jpg')

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
EnemyX_Change = 0.5
EnemyY_Change = 40


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
    # Background Image
    screen.blit(background, (0,0))
    # Game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Player Keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_Change += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # Change player location on map
    playerX += playerX_Change

    # Check if out of bound
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Change Enemy location on map
    EnemyX += EnemyX_Change
    # Check if out of bound
    if EnemyX <= 0:
        EnemyX_Change += 0.5
        EnemyY += EnemyY_Change
    elif EnemyX > 736:
        EnemyX_Change -= 0.5
        EnemyY += EnemyY_Change

    player(playerX, playerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()
