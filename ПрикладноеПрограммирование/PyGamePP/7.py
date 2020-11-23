import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])
fontObj = pygame.font.Font('tahoma.ttf', 20)
text = fontObj.render('Привет, ТАТК!', True, (255,255,0), (0,0,255))
screen.blit(text,[70, 100])
pygame.display.flip()
