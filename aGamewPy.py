import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

x = 50 
y = 50
width = 40 
height = 60 
vel = 5

run = True
while run:
    pygame.time.delay(100)
