import pygame
from kangaroo import kangaroo
from boomerang import Boomerang
from background import Background

pygame.init()
#Sets up the screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Kangaroo Game')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

backGround = Background('../assets/img/background.png')

global player1
global player2

speed = 50
boomerang = Boomerang(speed, 50, 360)
boomerangsprite = pygame.sprite.RenderPlain(boomerang)

player1 = kangaroo("left", boomerang)
player2 = kangaroo("right", boomerang)




playersprites = pygame.sprite.RenderPlain((player1, player2))

screen.blit(background, (0, 0))
pygame.display.flip()
screen.blit(backGround.image, backGround.rect)

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
            if event.key == pygame.K_SPACE and boomerang.reversed and boomerang.orignalx == boomerang.rect.x and player1.canShootAgain:
                boomerang = Boomerang(speed, player1.rect.centerx, player1.rect.centery)
                player1.canShootAgain = False
                boomerangsprite = pygame.sprite.RenderPlain(boomerang)
                boomerangsprite.update()
                boomerangsprite.draw(screen)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                player1.movepos = [0,0]
                player1.state = "still"
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.movepos = [0,0]
                player2.state = "still"

    screen.blit(backGround.image, backGround.rect)
    screen.blit(background, boomerang.rect, boomerang.rect, pygame.BLEND_ADD)
    screen.blit(background, player1.rect, player1.rect, pygame.BLEND_ADD)
    screen.blit(background, player2.rect, player2.rect, pygame.BLEND_ADD)
    playersprites.update()
    boomerangsprite.update()
    boomerangsprite.draw(screen)
    playersprites.draw(screen)
    pygame.display.flip()
    print("CAN I SHOOT: " + str(player1.canShootAgain))

if __name__ == '__main__': main()