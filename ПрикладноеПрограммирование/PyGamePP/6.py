import pygame
import math
screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])
plotPoint = []
for x in range(0,300):
    y = int(math.sin(x / 300 * 4 * math.pi) * 150 + 150)
    plotPoint.append([x,y])
pygame.draw.lines(screen, [0,0,0], False, plotPoint, 1)
pygame.display.flip()
