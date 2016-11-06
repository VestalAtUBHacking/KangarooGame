import pygame

pygame.init()
#Sets up the screen
screen = pygame.display.set_mode((1280, 720))
done = False

#While the game is running
while not done:
    for event in pygame.event.get():
        #Quits the game
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
