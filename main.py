import pygame
# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:

    # RGB- red, green, blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()


