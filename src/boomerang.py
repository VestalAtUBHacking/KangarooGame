import pygame
from utilities import load_png

class Boomerang(pygame.sprite.Sprite):
    """A boomerang that will move in a parabolic arc
    and return to the thrower"""
    def __init__(self, (xy), vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/img/Boomerang.gif')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

    def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('../assets/img/boomerang.png')
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.vector = vector

        def update(self):
		newpos = self.calcnewpos(self.rect,self.vector)
		self.rect = newpos

        def calcnewpos(self,rect,vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)