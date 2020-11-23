import pygame
pygame.init()
screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("ball.png")
screen.blit(my_ball, [2, 2])
pygame.display.flip()
