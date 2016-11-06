class Boomerang(pygame.sprite.Sprite):
    """A boomerang that will move in a parabolic arc
    and return to the thrower"""
    def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('Boomerang.png')
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

        def throwAction(self, rect, position):
			background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
            screen = create_graphics_screen()
 			for i in range(6):
 			screen.blit(background[i], (i*10, 0))
 			playerpos = 3
 			screen.blit(playerimage, (playerpos*10, 0))