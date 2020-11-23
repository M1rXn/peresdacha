import pygame
pygame.init()
screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255,0,0],[100,100], 30, 1)
pygame.draw.rect(screen, [0,255,0], [100, 100, 50, 50], 0)
plotPoints=[[0,0],[30,30],[60,0],[90,30],[120,0]]
pygame.draw.lines(screen, [0,0,255], False, plotPoints,2)
pygame.display.flip()
