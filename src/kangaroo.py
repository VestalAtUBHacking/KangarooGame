import pygame
from utilities import load_png

class kangaroo(pygame.sprite.Sprite):
    
    def __init__(self, side, boomerang):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/img/Kangaroo.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 5
        self.state = "still"
        self.reinit()
        self.imageCounter = 0
        self.canShootAgain = False
        self.boom = boomerang
        self.counter = 10

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):
        self.counter = self.counter + 1
        self.image = pygame.image.load("../assets/img/kangaroo-frame-" + str(self.imageCounter) + ".png")
        if self.counter % 10 == 0:
            self.imageCounter = self.imageCounter + 1
        if(self.imageCounter == 4):
            self.imageCounter = 0
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        if self.rect.colliderect(self.boom.rect):
            self.canShootAgain = True
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"

    def moveleft(self):
        self.movepos[0] = self.movepos[0] - (self.speed)
        self.state = "moveleft"

    def moveright(self):
        self.movepos[0] = self.movepos[0] + (self.speed)
        self.state = "moveright"