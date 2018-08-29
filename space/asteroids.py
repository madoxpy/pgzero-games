from random import randint,choice
import numpy as np

HEIGHT=850
WIDTH=850
TITLE="Asteroids"

# TO DO:
# - umieranie


class Ship(Actor):
    clock = 0
    lastshot = 0
    shooting_speed = 25
    v = 0
    health = 5
    alive = True
    time_of_death = 0
    points = 0
    level = 1

    def shoot(self,alpha):
        if self.clock-self.lastshot>self.shooting_speed:
            s = Shot("shot.png")
            s.angle = alpha
            s.x, s.y = ship.center
            s.v = ship.v + 2
            shots.append(s)
            self.lastshot = self.clock
    def update(self):
        self.clock=self.clock+1
        self.center=(self.center[0]-np.sin(np.deg2rad(self.angle))*self.v,self.center[1]-np.cos(np.deg2rad(self.angle))*self.v)
        if self.center[0]<0:
            self.center=(self.center[0]+WIDTH,self.center[1])
        if self.center[0]>WIDTH:
            self.center=(0,self.center[1])   

        if self.center[1]<0:
            self.center=(self.center[0],self.center[1]+HEIGHT)
        if self.center[1]>HEIGHT:
            self.center=(self.center[0],0) 

        alpha = self.angle
        if self.alive:
            self.image="ship"+str(int(self.v))+".png"
        else:
            self.image = "ship0dead.png"
        self.angle = alpha

        for rock in rocks:
            if self.colliderect(rock) and self.alive:
                self.alive = False
                self.time_of_death = self.clock
                self.health -= 1
                rocks.remove(rock)
                if int(rock.image[4]) <= 3:
                    for i in range(2):
                        r = Rock("rock"+str(int(rock.image[4])+1)+".png")
                        r.x=rock.x
                        r.y=rock.y
                        r.vx = randint(-2,2)
                        r.vy = randint(-2,2)
                        r.rot = choice([-1,1])
                        rocks.append(r)
        
        if self.clock - self.time_of_death > 100:
            self.alive = True



    def acc(self):
        self.v = self.v + 0.02
        if self.v > 3.9999:
            self.v = 3.9999

    def brake(self):
        self.v = self.v - 0.02
        if self.v < 0:
            self.v = 0

ship=Ship("ship.png",center=(WIDTH/2,HEIGHT/2))



class Shot(Actor):
    #x, y = ship.center
    #v = 3   # PREDKOSC
    
    def update(self):
        vx = -self.v*np.sin(np.deg2rad(self.angle))
        vy = -self.v*np.cos(np.deg2rad(self.angle))
        self.x=self.x+vx
        self.y=self.y+vy
        self.center=(self.x,self.y)    
        if not 0<self.x<WIDTH or  not 0<self.y<HEIGHT:
            shots.remove(self)


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
                ship.points += 1
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
    if ship.health > 0:
        ship.draw()
    else:
        screen.draw.text("GAME OVER",color="white",midtop=(WIDTH//2,200),fontsize=70)
    for rock in rocks:
        rock.draw()
    for shot in shots:
        shot.draw()

    screen.draw.text(str(ship.points),color="white",midtop=(WIDTH-40,HEIGHT-20),fontsize=20)


    for i in range(ship.health):
        screen.blit("heart.png",(i*20,HEIGHT-20))

def update():
    if ship.health > 0:
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

    if len(rocks)==0:
        ship.level += 1
        for i in range(ship.level):
            rocks.append(Rock("rock1.png"))

    #print(rocks[0].center)

bg=Actor("background.png",center=(WIDTH/2,HEIGHT/2))
rocks=[Rock("rock1.png")]
shots=[]

