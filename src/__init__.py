import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False

kang = pygame.image.load("../assets/img/Kangaroo.gif")
kangrect = kang.get_rect()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

    screen.blit(kang, kangrect)