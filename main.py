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

# Add enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 0.5
enemyY_Change = 40

# Bullet
# Ready - can't see the bullet
# Fire - Bullet is on screen
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 2
bullet_state = "ready"


# Player function
def player(x, y):
    screen.blit(playerImg, (x, y))


# Player function
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # RGB - build initial screen
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    # Game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Player Keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_Change += 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
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

    # Change enemy location on map
    enemyX += enemyX_Change
    # Check if out of bound
    if enemyX <= 0:
        enemyX_Change += 0.5
        enemyY += enemyY_Change
    elif enemyX > 736:
        enemyX_Change -= 0.5
        enemyY += enemyY_Change

    # Bullet Movement
    # bullet reset
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
