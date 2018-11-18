import random
import numpy as np
HEIGHT=753
WIDTH=1200
TITLE="Duck"
bluesky = (135,206,235)
BLUE = 64, 164, 223
BOX = Rect((0, 500), (WIDTH, 500))




class Bullet(Actor):
    dirx = random.randint(-5,5)
    diry = random.randint(-5,-1)

    def update(self):
        self.left = self.left + self.dirx
        #self.top = self.top + self.diry
        uy=self.diry
        self.diry=self.diry+0.1
        self.top=self.top+(uy+self.diry)*0.5





def draw():
    screen.fill(bluesky)
    for b in bullets:
        b.draw()


def update(dt):
    if keyboard.space:
        b = Bullet("bullet.png")
        v = 10
        angle = random.randint(-70+180,70+180)
        b.dirx = v * np.sin(np.deg2rad(angle))
        b.diry = v * np.cos(np.deg2rad(angle))
        b.pos = (WIDTH//2,750)
        bullets.append(b)
    for b in bullets:
        b.update()

bullets = []
