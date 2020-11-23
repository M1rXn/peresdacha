import pygame
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        

screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])        
ima_file = "ball.png"
location = [10, 10]
ball = MyBallClass(ima_file, location)
screen.blit(ball.image,ball.rect)
pygame.display.flip()
        
        
