import random
import numpy as np
HEIGHT=753
WIDTH=1200
TITLE="Duck"
bluesky = (135,206,235)
BLUE = 64, 164, 223
BOX = Rect((0, 500), (WIDTH, 500))

class Duck(Actor):
	alive = True
	frame = 0
	images = ["duck00.png","duck01.png","duck02.png","duck03.png"]
	score = 0
	def up(self):
		if self.bottom > 30:
			self.top=self.top-5

	def down(self):
		if self.top < 550:
			self.top=self.top+5

	def l(self):
		if self.right > 30:
			self.left=self.left-3

	def r(self):
		if self.left < WIDTH-30:
			self.left=self.left+5

	def update(self,bullets):
		self.image=self.images[int(self.frame)]
		self.frame= (self.frame+0.1) % len(self.images)
		for b in bullets:
			if b.colliderect(self):
				self.alive=False
				hunter.f = 40
		if not self.alive:
			for i in range(len(bullets)):
				bullets.pop()
		else:
			self.score = len(bullets)

		
class Bullet(Actor):
	dirx = random.randint(-5,5)
	diry = random.randint(-5,-1)
	
	def update(self):
		self.left = self.left + self.dirx
		self.top = self.top + self.diry
		
		
class Hunter(Actor):
	dirx=2
	diry=0.5
	frame = 0
	f = 40
	def update(self,bullets):
		self.left=self.left+self.dirx
		if self.left<100:
			self.dirx=2
		if self.left>WIDTH-100:
			self.dirx=-2
		self.top=self.top+self.diry
		if self.top<600:
			self.diry=0.5
		if self.top>700:
			self.diry=-0.5
		self.frame= self.frame+1
		
		if duck.score % 10 == 0:
			self.f = self.f - 0.1
		if self.f<=0:
			self.f = 1
		if self.frame % int(self.f) == 0:
			b = Bullet("bullet.png")
			v = 10
			angle = random.randint(-70+180,70+180)
			b.dirx = v * np.sin(np.deg2rad(angle))
			b.diry = v * np.cos(np.deg2rad(angle))
			b.pos = self.center#(self.left,self.top)
			bullets.append(b)



		
		
def draw():
	screen.fill(bluesky)


	screen.draw.filled_rect(BOX, BLUE)

	bgr.draw()
	bgr2.draw()
	tree.draw()
	tree2.draw()
	tree3.draw()
	tree4.draw()
	if duck.alive:
		duck.draw()
		hunter.draw()
		for b in bullets:
			b.draw()
	else:
		screen.draw.text("GAME OVER",(WIDTH//2-50,HEIGHT//2-50),color="black")
		screen.draw.text("Press [space] to start again",(WIDTH//2-100,HEIGHT//2),color="black")
	screen.draw.text(str(duck.score),(WIDTH-50,20),color="black")


def update():
	duck.update(bullets)
	hunter.update(bullets)
	if duck.alive:
		for b in bullets:
			b.update()
		bgr.left = bgr.left - 0.5
		if bgr.left < -1700:
			bgr.left = bgr.left + 2*1539	
		bgr2.left = bgr2.left - 0.5
		if bgr2.left < -1700:
			bgr2.left = bgr2.left + 2*1539	


		tree.left = tree.left - 1
		tree2.left = tree2.left - 1
		tree3.left = tree3.left - 1
		tree4.left = tree4.left - 1

		if tree.left < -1000:
			tree.left = tree.left + 4*665	
		if tree2.left < -1000:
			tree2.left = tree2.left + 4*665	
		if tree3.left < -1000:
			tree3.left = tree3.left + 4*665	
		if tree4.left < -1000:
			tree4.left = tree4.left + 4*665	

		if keyboard.up:
			duck.up()
		if keyboard.down:
			duck.down()
		if keyboard.left:
			duck.l()
		if keyboard.right:
			duck.r()
	else:
		if keyboard.space:
			#bullets = []
			duck.alive = True

duck = Duck("duck00.png")
bgr = Actor("mount.png")
bgr.pos = (0,400)
bgr2 = Actor("mount2.png")
bgr2.pos = (1539,400)

tree = Actor("tree.png")
tree.pos = (0,550)
tree2 = Actor("tree2.png")
tree2.pos = (665,550)
tree3 = Actor("tree.png")
tree3.pos = (665*2,550)
tree4 = Actor("tree2.png")
tree4.pos = (665*3,550)
#bgr.pos = 

bullets = []
hunter = Hunter("boat.png")
hunter.pos = (100,700)