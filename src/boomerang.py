import pygame
from utilities import load_png

class Boomerang(pygame.sprite.Sprite):
    """A boomerang that will move in a parabolic arc
    and return to the thrower"""
    #Hey that's pretty good
    def __init__(self, speed, x, y):
        self.x = x
        self.imageCounter = 0
        self.y = y
        self.orignalx = x
        self.orignaly = y
        self.reversed = False
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/img/boomerangframe-0.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.movepos = [self.x,self.y]
        self.rect.x = self.x
        self.rect.y = self.y - 20

    def update(self):
        self.image = pygame.image.load("../assets/img/boomerangframe-" + str(self.imageCounter) + ".png")
        self.imageCounter = self.imageCounter + 1
        if(self.imageCounter == 3):
            self.imageCounter = 0
        if self.reversed == True:
            if self.rect.x == self.orignalx:
                self.rect.x = self.orignalx
                self.image = pygame.image.load('../assets/img/boomerangframe-0.png')
            else:
                self.rect.x -= 20   
        else:
            self.rect.x += 20
            if(self.rect.x >= self.orignalx + 640):
                self.reversed = True
        pygame.event.pump()