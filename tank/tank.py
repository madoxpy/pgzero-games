import numpy as np
import random
import pygame

HEIGHT=800
WIDTH=800
TITLE="TANK"



class Bullet(Actor):
    dirx = 0
    diry = 0
    color = (0,0,0)

    def update(self):
        self.left = self.left + self.dirx
        self.top = self.top + self.diry




def update():
    if keyboard.left:
        tank.angle += 1
    if keyboard.right:
        tank.angle -= 1
    if keyboard.up:
        a = np.deg2rad(tank.angle)
        x = np.sin(a)*10
        y = np.cos(a)*10
        for obj in objs:
            obj.pos = (obj.pos[0]+x,obj.pos[1]+y)
        for obj in objs:
            if np.sqrt((WIDTH//2-obj.left)**2+(HEIGHT//2-obj.center[1])**2) < 50 or np.sqrt((WIDTH//2-obj.right)**2+(HEIGHT//2-obj.center[1])**2) < 50 or np.sqrt((WIDTH//2-obj.center[0])**2+(HEIGHT//2-obj.top)**2) < 50 or np.sqrt((WIDTH//2-obj.center[0])**2+(HEIGHT//2-obj.bottom)**2) < 50:
                for obj2 in objs:
                    obj2.pos = (obj2.pos[0]-x*0.5,obj2.pos[1]-y*0.5)
                obj.pos = (obj.pos[0]-x*2,obj.pos[1]-y*2)
                break


    x = pygame.mouse.get_pos()[0] - WIDTH//2
    y = pygame.mouse.get_pos()[1] - HEIGHT//2
    if y == 0:
        y = 1
    if y > 0:
        cannon.angle = np.rad2deg(np.arctan(x/y)+135)
    else:
        cannon.angle = np.rad2deg(np.arctan(x/y))

    for a in ammo:
        a.update()
        if a.left<0 or a.left>WIDTH or a.top<0 or a.top > HEIGHT:
            ammo.remove(a)

    for a in ammo:
        for obj in objs:
            if a.colliderect(obj):
                ammo.remove(a)
                objs.remove(obj)




def on_mouse_down(pos, button):

    x = pygame.mouse.get_pos()[0] - WIDTH//2
    y = pygame.mouse.get_pos()[1] - HEIGHT//2
    if y==0:
        y=1
    bullet=Bullet("bullet.png",center=(WIDTH//2,HEIGHT//2))
    v = 12
    angle = np.rad2deg(np.arctan(x/y))
    if y < 0 and x > 0:
        angle = angle+180
    if y < 0 and x < 0:
        angle += 180


    bullet.dirx = v * np.sin(np.deg2rad(angle))
    bullet.diry = v * np.cos(np.deg2rad(angle))
    ammo.append(bullet)


def draw():
    screen.fill((100,170,100))
    tank.draw()
    #screen.draw.circle((WIDTH//2,HEIGHT//2),50,(0,0,0))

    #screen.draw.rect(tank.rect,(0,0,0))
    cannon.draw()
    for obj in objs:
        obj.draw()
    for a in ammo:
        a.draw()



tank=Actor("tank.png",center=(WIDTH//2,HEIGHT//2))
cannon=Actor("cannon.png",center=(WIDTH//2,HEIGHT//2))
objs=[Actor("box.png",center=(random.randint(-1000,1000),random.randint(-1000,1000))) for i in range(100)]
ammo = []