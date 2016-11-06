import pygame
from kangaroo import kangaroo
from boomerang import Boomerang
from gondola import gondola
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

gondola = gondola()
gondolasprite = pygame.sprite.RenderPlain(gondola)

speed = 1
boomerang = Boomerang(speed, 50, 360)
boomerangTwo = Boomerang(-speed, 1230, 360)
boomerangsprite = pygame.sprite.RenderPlain(boomerang)
boomerangTwoSprite = pygame.sprite.RenderPlain(boomerangTwo)

player1 = kangaroo("left", boomerang)
player2 = kangaroo("right", boomerangTwo)



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
                player2.image = pygame.transform.flip(player2.image, False, True)
            if event.key == pygame.K_RIGHT:
                player2.moveright()
            if event.key == pygame.K_SPACE and boomerang.reversed and boomerang.orignalx == boomerang.rect.x and player1.canShootAgain:
                boomerang = Boomerang(speed, player1.rect.centerx, player1.rect.centery)
                player1.canShootAgain = False
                boomerangsprite = pygame.sprite.RenderPlain(boomerang)
                boomerangsprite.update()
                boomerangsprite.draw(screen)
            if event.key == pygame.K_RSHIFT and boomerangTwo.reversed and boomerangTwo.orignalx == boomerangTwo.rect.x and player2.canShootAgain:
                boomerangTwo = Boomerang(speed, player2.rect.centerx, player2.rect.centery)
                player2.canShootAgain = False
                boomerangTwoSprite = pygame.sprite.RenderPlain(boomerangTwo)
                boomerangTwoSprite.update()
                boomerangTwoSprite.draw(screen)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                player1.movepos = [0,0]
                player1.state = "still"
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.movepos = [0,0]
                player2.state = "still"

    screen.blit(backGround.image, backGround.rect)
    screen.blit(background, boomerang.rect, boomerang.rect, pygame.BLEND_ADD)
    screen.blit(background, boomerangTwo.rect, boomerangTwo.rect, pygame.BLEND_ADD)
    screen.blit(background, player1.rect, player1.rect, pygame.BLEND_ADD)
    screen.blit(background, player2.rect, player2.rect, pygame.BLEND_ADD)
    gondolasprite.update()
    playersprites.update()
    boomerangsprite.update()
    boomerangTwoSprite.update()
    boomerangTwoSprite.draw(screen)
    boomerangsprite.draw(screen)
    playersprites.draw(screen)
    gondolasprite.draw(screen)
    pygame.display.flip()

if __name__ == '__main__': main()