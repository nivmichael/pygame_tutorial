import pygame
import random
import math
from pygame import mixer

# Init
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background Image
background = pygame.image.load('background.jpg')

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Add Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

# Add enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_Change.append(0.5)
    enemyY_Change.append(40)

# Bullet
# Ready - can't see the bullet
# Fire - Bullet is on screen
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 2
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


# show the score on screen
def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Player function
def player(x, y):
    screen.blit(playerImg, (x, y))


# Player function
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


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
                playerX_Change -= 2
            if event.key == pygame.K_RIGHT:
                playerX_Change += 2
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                #get current coordinate of the spaceship
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

    # Change enemy location on map, and calculat collision
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_Change[i]
        # Check if out of bound
        if enemyX[i] <= 0:
            enemyX_Change[i] += 0.5
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] > 736:
            enemyX_Change[i] -= 0.5
            enemyY[i] += enemyY_Change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_sound = mixer.Sound('explosion.wav')
            bullet_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    # bullet reset
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
