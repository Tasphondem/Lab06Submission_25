import sys 
import pygame as pg
from lib import *
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
push_A = False
push_D = False
push_W = False
push_S = False
W,A,S,D = 0,0,0,0

while(run):
    screen.fill((255,255,255))
    Obj = Rectangle(20-A+D,20-W+S,100,100)
    Obj.r,Obj.g,Obj.b = 250,0,250
    Obj.draw(screen)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_a : 
            push_A = True
            #A += 1
        if event.type == pg.KEYUP and event.key == pg.K_a : #ปุ่มถูกปล่อยและเป็นปุ่ม A
            #print("Key A up")
            push_A = False
        if event.type == pg.KEYDOWN and event.key == pg.K_d : #ปุ่มถูกกดลงและเป็นปุ่ม D
            #print("Key D down")
            push_D = True
            #D += 1
        if event.type == pg.KEYUP and event.key == pg.K_d :
            push_D = False
        if event.type == pg.KEYDOWN and event.key == pg.K_w :
            push_W = True
            #W += 1
        if event.type == pg.KEYUP and event.key == pg.K_w :
            push_W = False
        if event.type == pg.KEYDOWN and event.key == pg.K_s :
            push_S = True
            #S += 1
        if event.type == pg.KEYUP and event.key == pg.K_s :
            push_S = False
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            
    if push_W == True:
        W += 1
    if push_A == True:
        A += 1
    if push_S == True:
        S += 1
    if push_D == True:
        D += 1

    pg.display.update()
    pg.time.delay(4)
 
