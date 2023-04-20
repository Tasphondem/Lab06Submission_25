import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r,self.g,self.b = 250,0,0
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouseX,mouseY = pg.mouse.get_pos()
        if (mouseX >= self.x and mouseX <= self.x+self.w ) and (mouseY >= self.y and mouseY <= self.y + self.h):
            return True
        else:
            return False
        
    # def isMouseOff(self):
    #     mouseX,mouseY = pg.mouse.get_pressed()
    #     if mouseX == 0 and mouseY == 0:
    #         return True
    #     else:
    #         return False











    