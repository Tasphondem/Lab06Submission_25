import sys 
import pygame as pg
from lib import *
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))

    if btn.isMouseOn():
        btn.r,btn.g,btn.b = (220,220,220)

        if pg.mouse.get_pressed() == (1,0,0):
            btn.r,btn.g,btn.b = (120,20,220)
    
    else:
        btn.r,btn.g,btn.b = (250,0,0)

    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False