import pygame
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 300:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 300:
            self.speed[1] = -self.speed[1]
        
screen = pygame.display.set_mode([300, 300])
screen.fill([255, 255, 255])
img_file = "ball.png"
location = [10, 10]        
speed = [2, 2]
ball = MyBallClass(img_file, location, speed) 
while True:
    pygame.time.delay(20)
    screen.fill([255,255,255])
    ball.move()
    screen.blit(ball.image,ball.rect)
    pygame.display.flip()

        
