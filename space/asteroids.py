from random import randint,choice
import numpy as np

HEIGHT=850
WIDTH=850
TITLE="Asteroids"

class Shot(Actor):
    x = WIDTH/2
    y = HEIGHT/2
    v = 3   # PREDKOSC
    
    def update(self):
        vx = -self.v*np.sin(np.deg2rad(self.angle))
        vy = -self.v*np.cos(np.deg2rad(self.angle))
        self.x=self.x+vx
        self.y=self.y+vy
        self.center=(self.x,self.y)    
        if not 0<self.x<WIDTH or  not 0<self.y<HEIGHT:
            shots.remove(self)

class Ship(Actor):
    clock = 0
    lastshot = 0
    shooting_speed = 25
    v = 0

    def shoot(self,alpha):
        if self.clock-self.lastshot>self.shooting_speed:
            s = Shot("shot.png")
            s.angle = alpha
            shots.append(s)
            self.lastshot = self.clock
    def update(self):
        self.clock=self.clock+1
        '''
        for rock in rocks:
            rock.x=rock.x+np.sin(np.deg2rad(self.angle))*self.v
            rock.y=rock.y+np.cos(np.deg2rad(self.angle))*self.v
        '''
        

    def acc(self):
        self.v = self.v + 0.1
        if self.v > 2:
            self.v = 2

    def brake(self):
        self.v = self.v - 0.1
        if self.v < 0:
            self.v = 0

class Rock(Actor):
    x=randint(0,WIDTH)
    y=randint(0,HEIGHT)
    while ((x-WIDTH)**2+(y-HEIGHT)**2)<90000: 
        x=randint(0,WIDTH)
        y=randint(0,HEIGHT)   
    vx = randint(-2,2)
    vy = randint(-2,2)
    rot = choice([-1,1])

    def update(self):
        self.angle=self.angle+self.rot
        self.x=(self.x+self.vx)%WIDTH
        self.y=(self.y+self.vy)%HEIGHT
        self.center=(self.x,self.y)
        for shot in shots:
            if self.colliderect(shot):
                rocks.remove(self)
                if int(self.image[4]) <= 3:
                    for i in range(2):
                        r = Rock("rock"+str(int(self.image[4])+1)+".png")
                        r.x=self.x
                        r.y=self.y
                        r.vx = randint(-2,2)
                        r.vy = randint(-2,2)
                        r.rot = choice([-1,1])
                        rocks.append(r)
                shots.remove(shot)

def draw():
    #screen.fill((148, 146, 255))
    bg.draw()
    ship.draw()
    for rock in rocks:
        rock.draw()
    for shot in shots:
        shot.draw()

def update():
    if keyboard.left:
        ship.angle=(ship.angle+2)%360
    if keyboard.right:
        ship.angle=(ship.angle-2)%360
    if keyboard.space:
        ship.shoot(ship.angle)
    if keyboard.up:
        ship.acc()
    if keyboard.down:
        ship.brake()

    for rock in rocks:
        rock.update()
    for shot in shots:
        shot.update()
    ship.update()
    #print(rocks[0].center)

bg=Actor("background.png",center=(WIDTH/2,HEIGHT/2))
ship=Ship("ship.png",center=(WIDTH/2,HEIGHT/2))
rocks=[Rock("rock1.png")]
shots=[]

