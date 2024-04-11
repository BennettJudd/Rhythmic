import pygame

class Button:
    def __init__(self,x,y,w,h,r,b,g):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.b = b
        self.g = g
    

    def create_rect(self, surface):
        return pygame.draw.rect(surface, (self.r,self.b,self.g), [self.x, self.y, self.w, self.h])


