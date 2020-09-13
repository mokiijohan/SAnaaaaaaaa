import pygame
pygame.init()
w = pygame.display.set_mode([1520,900])
white = (255,255,255)
black = (000,000,000)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
gray = (125,125,125)
green = (0,255,0)
pygame.draw.line(w,blue,[100,50],[200,50],2)
pygame.display.update()

pygame.draw.line(w,blue,[100,50],[100,150],2)
pygame.display.update()

pygame.draw.line(w,blue,[100,150],[200,150],2)
pygame.display.update()

pygame.draw.line(w,blue,[200,50],[200,150],2)
pygame.display.update()

pygame.draw.rect(w,red,[250,50,100,100],2)
pygame.display.update()

pygame.draw.rect(w,green,[200,75,50,25],2)
pygame.display.update()

pygame.draw.circle(w,yellow,[150,75],25,3)
pygame.display.update()

pygame.draw.circle(w,yellow,[275,75],25)
pygame.display.update()






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

