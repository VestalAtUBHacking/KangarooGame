import pygame
from utilities import load_png

class gondola(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/img/gondolaframe-1.png')
        screen = pygame.display.get_surface()
        self.originalX = 500
        self.area = screen.get_rect()
        self.state = "still"
        self.reinit()
        self.imageCounter = 0
        self.rect.y = 212
        self.rect.x = 500
        self.reversed = False

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]

    def update(self):
        self.image = pygame.image.load("../assets/img/gondolaframe-" + str(self.imageCounter) + ".png")
        self.imageCounter = self.imageCounter + 1
        if(self.imageCounter == 7):
            self.imageCounter = 0
        if self.reversed == True:
            self.image = pygame.transform.flip(self.image, True, False)
            if self.rect.x == self.originalX:
                self.rect.x = self.originalX
                self.reversed = False
            else:
                self.rect.x -= 2   
        else:
            self.rect.x += 2
            if(self.rect.x >= self.originalX + 200):
                self.reversed = True
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