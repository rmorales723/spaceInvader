import pygame
# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# RGB- red, green, blue
    screen.fill((0, 0, 0))
    pygame.display.update()
