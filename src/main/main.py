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
SS = True
NP = True
pygame.display.set_caption('~-Rhythmic-~')
while True:
    for event in pygame.event.get():
        color = (0,0,0)
        surface.fill(color)
        
    if NP == True:     
       
        if SS == True:

        
          
            rbg += .3 * rbgmult

            if rbg >= 255 or rbg <= 1:
                rbgmult *= -1           
            pygame.draw.rect(surface,(rbg,200,200),[10,10,580,580],10)
        

            b1 = Button(250,300,100,20,rbg,210,210)
            b1.create_rect(surface)
     

            text = font.render('Press any key to start the game', True, (255, 255, 255))
            text_rect = text.get_rect(center=(1920//2, 1080//2 + 100))
            surface.blit(text, text_rect)  
      
        
        
            if event.type == pygame.MOUSEBUTTONUP:
                SS = False


    pygame.display.update()
    
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
pygame.display.update()
