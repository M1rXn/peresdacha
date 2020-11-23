import math
import pygame
import os
screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])
for x in range(0,300):
    y = int(math.sin(x / 300.0 * 4 * math.pi) * 150 + 150)
    screen.set_at([x,y], [0, 0, 0])
    pygame.display.flip()
