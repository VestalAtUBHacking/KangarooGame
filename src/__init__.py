import pygame
from kangaroo import kangaroo

pygame.init()
#Sets up the screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Kangaroo Game')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

global player1
global player2

player1 = kangaroo("left")
player2 = kangaroo("right")

playersprites = pygame.sprite.RenderPlain((player1, player2))

screen.blit(background, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

done = False

#While the game is running
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.moveup()
            if event.key == pygame.K_s:
                player1.movedown()
            if event.key == pygame.K_a:
                player1.moveleft()
            if event.key == pygame.K_d:
                player1.moveright()
            if event.key == pygame.K_UP:
                player2.moveup()
            if event.key == pygame.K_DOWN:
                player2.movedown()
            if event.key == pygame.K_LEFT:
                player2.moveleft()
            if event.key == pygame.K_RIGHT:
                player2.moveright()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                player1.movepos = [0,0]
                player1.state = "still"
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.movepos = [0,0]
                player2.state = "still"


    screen.blit(background, player1.rect, player1.rect)
    screen.blit(background, player2.rect, player2.rect)
    playersprites.update()
    playersprites.draw(screen)
    pygame.display.flip()

if __name__ == '__main__': main()