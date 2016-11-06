class Boomerang(pygame.sprite.Sprite):
    """A boomerang that will move in a parabolic arc
    and return to the thrower"""
    def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.boomerang = load_png('Boomerang.gif')
		screen = pygame.display.get_surface()
		self.area = screen.get_boomerang()
		self.vector = vector