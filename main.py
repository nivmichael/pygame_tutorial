import pygame

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


# Player function
def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    # RGB - build initial screen
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX += 5
                player(playerX, playerY)
            if event.key == pygame.K_LEFT:
                playerX -= 5
                player(playerX, playerY)

    player(playerX, playerY)
    pygame.display.update()
