import numpy as np
from random import randint
import pygame as pg
from time import time
HEIGHT=1000
WIDTH=1800
TITLE="Race"

time_start = time()+5
MAXSPEED = 16

class Car(Actor):
    v=0
    chp = np.zeros(8)
    finish = 0

    def update(self,bg,p21,p12,p2):
        bg.center=(bg.center[0]+np.sin(np.deg2rad(self.angle))*self.v,bg.center[1]+np.cos(np.deg2rad(self.angle))*self.v)
        p21.center=(p21.center[0]+np.sin(np.deg2rad(self.angle))*self.v,p21.center[1]+np.cos(np.deg2rad(self.angle))*self.v)
        p21.center=(p21.center[0]-np.sin(np.deg2rad(p21.angle))*p21.v,p21.center[1]-np.cos(np.deg2rad(p21.angle))*p21.v)
        
        
        if self.v > 0:
            self.v=self.v-0.01
        elif self.v < 0:
            self.v=self.v+0.01

        if p21.v > 0:
            p21.v=p21.v-0.01
        elif p21.v < 0:
            p21.v=p21.v+0.01


        x_front1 = int(self.center[0]-np.sin(np.deg2rad(self.angle))*30)
        y_front1 = int(self.center[1]-np.cos(np.deg2rad(self.angle))*30)

        x_back2 = int(p21.center[0]+np.sin(np.deg2rad(p21.angle))*30)
        y_back2 = int(p21.center[1]+np.cos(np.deg2rad(p21.angle))*30)

        if (x_front1-x_back2)**2 + (y_front1-y_back2)**2 < 900:
            p12.v = p12.v*0.1
            self.v = self.v*0.1


        x_back1 = int(self.center[0]+np.sin(np.deg2rad(self.angle))*30)
        y_back1 = int(self.center[1]+np.cos(np.deg2rad(self.angle))*30)

        x_front2 = int(p21.center[0]-np.sin(np.deg2rad(p21.angle))*30)
        y_front2 = int(p21.center[1]-np.cos(np.deg2rad(p21.angle))*30)

        if (x_front1-x_front2)**2 + (y_front1-y_front2)**2 < 900:
            p12.v = p12.v*0.98
            p1.v = p1.v*0.98
            p21.v = p21.v*0.98
            p2.v = p2.v*0.98            

        x = int(self.center[0]-np.sin(np.deg2rad(p1.angle))*50)
        y = int(self.center[1]-np.cos(np.deg2rad(p1.angle))*50)
        screen.draw.circle((x,y), 10, (255, 255, 255))
        #print (x,y,screen.surface.get_at((x,y)))
        if not screen.surface.get_at((x,y)) == (148,167,163):
            if self.v > 0:
                self.v = self.v - 0.03
                p12.v = p12.v - 0.03

        for i in range(247,255):
            if screen.surface.get_at((x,y)) == (i,255,255) or screen.surface.get_at((x,y)) == (i,255,254):
                self.chp[i-247]=1
                print("checkpoint! "+str(i-247)+" "+str(i))
        
        if sum(self.chp)>=6 and self.finish == 0 and p2.finish == 0:
            if screen.surface.get_at((x,y)) == (255,255,255):
                self.finish = 1


    def acc(self):
        self.v = self.v + 0.05
        if self.v > MAXSPEED:
            self.v = MAXSPEED

    def brake(self):
        self.v = self.v - 0.06
        if self.v < -1:
            self.v = -1

def draw():
    screen.fill((58, 131, 61))

    #bg1.draw()
    part1=pg.Surface((WIDTH/2,HEIGHT))
    part1.blit(bg1._surf,bg1.center,(0,0,bg1.width,bg1.height))
    part2=pg.Surface((WIDTH/2,HEIGHT))
    part2.blit(bg2._surf,bg2.center,(0,0,bg2.width,bg2.height))


    screen.blit(part1,(0,0))
    screen.blit(part2,(WIDTH/2,0))

    rect = Rect((WIDTH/2-5,0),(10,HEIGHT))
    screen.draw.filled_rect(rect,(0,0,0))

    p1.draw()
    if p21.center[0]-5<WIDTH/2:
        p21.draw()


    p2.draw()
    if p12.center[0]+5>WIDTH/2:
        p12.draw()


    screen.blit("s1.png",(WIDTH/2-230, HEIGHT-200))
    screen.blit("s1.png",(WIDTH-230, HEIGHT-200))
    arr1.draw()
    arr2.draw()

    screen.blit("timer.png",((WIDTH/2-160, 10)))

    if (time()-time_start) >= 0.0:
        screen.draw.text(str(int(int(time()-time_start)/60)).zfill(2),color="green",midtop=(WIDTH//2+5,30),fontsize=60)
        screen.draw.text(":"+str(int(time()-time_start)%60).zfill(2),color="green",midtop=(WIDTH//2+58,30),fontsize=60)
    else:
        screen.draw.text(str(int(time()-time_start)).zfill(2),color="red",midtop=(WIDTH//2+5,30),fontsize=60)

    if p1.finish == 1:
        screen.draw.text("Player 1 won!",color="red",midtop=(WIDTH//2+5,300),fontsize=60)
    if p2.finish == 1:
        screen.draw.text("Player 2 won!",color="red",midtop=(WIDTH//2+5,300),fontsize=60)
def update():
    if time()-time_start >=0:
        if keyboard.a:
            p1.angle=(p1.angle+2)%360
            p12.angle=(p12.angle+2)%360
        if keyboard.d:
            p1.angle=(p1.angle-2)%360
            p12.angle=(p12.angle-2)%360
        if keyboard.w:
            p1.acc()
            p12.acc()
        if keyboard.s:
            p1.brake()
            p12.brake()

        if keyboard.left:
            p2.angle=(p2.angle+2)%360
            p21.angle=(p21.angle+2)%360
        if keyboard.right:
            p2.angle=(p2.angle-2)%360
            p21.angle=(p21.angle-2)%360
        if keyboard.up:
            p2.acc()
            p21.acc()
        if keyboard.down:
            p2.brake()
            p21.brake()

    p1.update(bg1,p21,p12,p2)
    p2.update(bg2,p12,p21,p1)

    arr1.angle=150-p1.v*240/MAXSPEED
    arr2.angle=150-p2.v*240/MAXSPEED



bg1=Actor("bg.jpg",center=(-WIDTH+200,-HEIGHT-435))
bg2=Actor("bg.jpg",center=(-WIDTH+200+65,-HEIGHT-435-85))

p1=Car("car1.png",center=(WIDTH/4,HEIGHT/2))
p21=Car("car2.png",center=(WIDTH/4-65,HEIGHT/2+85))
p2=Car("car2.png",center=(WIDTH/4*3,HEIGHT/2))
p12=Car("car1.png",center=(WIDTH/4*3+65,HEIGHT/2-85))

p1.angle = p1.angle + 80
p12.angle = p12.angle + 80

p2.angle = p2.angle + 80
p21.angle = p21.angle + 80

arr1=Actor("s2.png",center=(WIDTH/2-125,HEIGHT-83))
arr2=Actor("s2.png",center=(WIDTH-125,HEIGHT-83))

arr1.angle = arr1.angle + 150
arr2.angle = arr2.angle + 150
