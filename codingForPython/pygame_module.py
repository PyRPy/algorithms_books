# pygame_module.py 
import pygame
from pygame.locals import *
pygame.init()
gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("games !")

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()

