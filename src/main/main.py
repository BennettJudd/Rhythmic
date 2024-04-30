import pygame
import sys
import time
from Button import Button
from random import randrange
from pygame.locals import QUIT

pygame.init()
surface = pygame.display.set_mode((600, 600))
font = pygame.font.Font(None, 36)


rbg = 1
rbgmult = 1
rbgt = 1
rbgtmult = 1
b = 210
g = 210
bu = 255
gu = 255
SS = True
NP = True
Menu = False
pygame.display.set_caption('~-Rhythmic-~')
while True:
    pygame.display.update()
    for event in pygame.event.get():

        color = (20,20,20)
        surface.fill(color)
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            
    if NP == True:


        rbg += .3 * rbgmult

        if rbg >= 255 or rbg <= 1:
            rbgmult *= -1
        rbgt += .3 * rbgtmult

        if rbgt >= 255 or rbgt <= 1:
            rbgtmult *= -1   

        if SS == True:

            
            
          
            
           
            

            b1 = Button(250,300,100,20,rbgt,b,g,False)
            b1.create_rect(surface)
            b1.is_over(mousex, mousey)
            if b1.over == True:
                print("hi")
                b = bu
                g = gu
                rbgt = 210
               
                if event.type == pygame.MOUSEBUTTONUP:
                    SS = False
                    Menu = True
                else:
                    b = 210
                    g = 210
            
            text = font.render('Start', True, (0, 0, 0))
            surface.blit(text, (272, 298))
        pygame.draw.rect(surface,(rbg,200,200),[10,10,580,580],10)
 
       
        if Menu == True:
            b2 = Button(100,175,75,75,rbgt,b,g,False)
            b2.create_rect(surface)
            b2.is_over(mousex, mousey)
            if b2.over == True:
                print("hi")
                b = bu
                g = gu
                rbgt = 210
    
    
    
    if event.type == QUIT:
         pygame.quit()
         sys.exit()
    pygame.display.flip()

