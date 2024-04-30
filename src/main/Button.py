
import pygame

class Button:
    def __init__(self,x,y,w,h,r,b,g,over):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.b = b
        self.g = g
        self.over = False

    def create_rect(self, surface):
        return pygame.draw.rect(surface, (self.r,self.b,self.g), [self.x, self.y, self.w, self.h])


    def is_over(self,x,y):
        if x > self.x and y > self.y and x < (self.x + self.w) and y < (self.y + self.h):
            print("yes")  
            self.over = True
           
            
        else:
            print(self.x)
            self.over = False



