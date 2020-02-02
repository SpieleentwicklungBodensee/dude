#!/usr/bin/env python3
import pygame
import os

os.chdir(os.path.dirname(__file__))
pygame.init()

screen = pygame.display.set_mode((800, 600))

font = pygame.font.Font(None, 50)

image = pygame.image.load('character2.png')

grassImage = pygame.image.load('grass.png')
wallImage = pygame.image.load('wall.png')
flowerImage = pygame.image.load('flower.png')
dudeImage = pygame.image.load('Dude.png')

level = ['##################################',
         '##################################',
         '##                  +         + ##',
         '##           +                  ##',
         '##   +     ########             ##',
         '##       + ########        #######',
         '##                  +      #######',
         '########                        ##',
         '########         ##             ##',
         '##               ##    +        ##',
         '##   +           ##      +      ##',
         '##       +       ##             ##',
         '##               ##             ##',
         '######    ################   #####',
         '######    ################   #####',
         '##                              ##'
         '##     +         +              ##',
         '##                       +      ##',
         '##  +                  ##       ##',
         '###########     +      ##    +  ##',
         '###########         #####       ##',
         '##                  #####       ##',
         '##            +            +    ##',
         '##    +            +            ##',
         '##################################',
         '##################################']

level = [list(row) for row in level]

flowers = 0
x = 82
y = 82
dirx = 0
diry = 0
youWon = False
youLost = False

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
               done = True
            elif event.key == pygame.K_LEFT:
                if event.type == pygame.KEYDOWN:
                    dirx = -1
                elif dirx == -1:
                    dirx = 0
            elif event.key == pygame.K_RIGHT:
                if event.type == pygame.KEYDOWN:
                    dirx = 1
                elif dirx == 1:
                    dirx = 0
            elif event.key == pygame.K_UP:
                if event.type == pygame.KEYDOWN:
                    diry = -1
                elif diry == -1:
                    diry = 0
            elif event.key == pygame.K_DOWN:
                if event.type == pygame.KEYDOWN:
                    diry = 1
                elif diry == 1:
                    diry = 0

    screen.fill((173, 25, 97))

    ty = 0
    for row in level:
        tx = 0
        for tile in row:
            if tile == '#':
                screen.blit(wallImage, [tx, ty])
            elif tile == ' ':
                screen.blit(grassImage, [tx, ty])
            elif tile == '+':
                screen.blit(flowerImage, [tx, ty])
            tx += 24
        ty += 24

    screen.blit(image, [x, y]) #draw image on backbuffer at position x, y
    x += dirx * 2 # x = x + dirx
    y += diry * 2 # dir = direction
    screen.blit(dudeImage, [730, 510])

    cornerUL = level[(y     ) // 24][(x     ) // 24] == '#'
    cornerUR = level[(y     ) // 24][(x + 32) // 24] == '#'
    cornerLL = level[(y + 32) // 24][(x     ) // 24] == '#'
    cornerLR = level[(y + 32) // 24][(x + 32) // 24] == '#'

    corners = [cornerUL, cornerUR, cornerLL, cornerLR]
    if any(corners):
        x -= dirx * 2
        y -= diry * 2

    if level[(y + 16) // 24][(x + 16) // 24] == '+':
        level[(y + 16) // 24][(x + 16) // 24] = ' ' 
        flowers += 1
    text = font.render(str(flowers), 1, (0, 0, 0))
    screen.blit(text, (750, 10))

    if abs((x + 16) - (730 + 16)) < 20 and abs((y + 16) - (510 + 16)) < 20:
        if flowers == 18:
            youWon = True
        else:
            youLost = True

    if youLost:
        text = font.render('Too bad. You got dumped', 1, (0, 0, 0), (173, 25, 97))
        screen.blit(text, (170, 100)) 
    elif youWon:
        text = font.render('You repaired your love.. for now', 1, (0, 0, 0), (173, 25, 97))
        screen.blit(text, (120, 100)) 


    pygame.display.flip() # exchange screen front to back (back now visable)

pygame.quit()
