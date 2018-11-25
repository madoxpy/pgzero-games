import random
HEIGHT=800
WIDTH=800
TITLE="Labirynth"

BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
GREY = (100,100,100)


class Piece(object):
	def __init__(self,x,y,tab):
		self.tab = tab
		self.x = x
		self.y = y
		self.color = GREY
	
	def draw(self, n):	
		screen.draw.filled_rect(Rect((self.x*n+n//3,self.y*n+n//3), (n//3+2, n//3+2)), self.color)
		if self.tab[0] == 1:
			screen.draw.filled_rect(Rect((self.x*n+n//3,self.y*n), (n//3+2, n//3+2)), self.color)
		if self.tab[1] == 1:
			screen.draw.filled_rect(Rect((self.x*n+n//3*2,self.y*n+n//3), (n//3+2, n//3+2)), self.color)
		if self.tab[2] == 1:
			screen.draw.filled_rect(Rect((self.x*n+n//3,self.y*n+n//3*2), (n//3+2, n//3+2)), self.color)
		if self.tab[3] == 1:
			screen.draw.filled_rect(Rect((self.x*n,self.y*n+n//3), (n//3+2, n//3+2)), self.color)
	
	def rotate(self):
		tmp = self.tab[1:]
		tmp.append(self.tab[0])
		self.tab = tmp
			
def update():
	for b in board:
		if b.x == E[0] and b.y == E[1]:
			b.color = GREEN
		elif b.x == S[0] and b.y == S[1]:
			b.color = BLUE
		else:
			b.color = GREY


	for i in range(14):
		for b1 in board:
			for b2 in board:
				if b1.tab[0] == 1 and b2.tab[2] == 1 and (b1.color == GREEN or b2.color == GREEN):
					if b1.x == b2.x and b1.y == b2.y + 1:
						b1.color = GREEN
						b2.color = GREEN
				elif b1.tab[1] == 1 and b2.tab[3] == 1 and (b1.color == GREEN or b2.color == GREEN):
					if b1.x+1 == b2.x and b1.y == b2.y:
						b1.color = GREEN
						b2.color = GREEN
				elif b1.tab[0] == 1 and b2.tab[2] == 1 and (b1.color == BLUE or b2.color == BLUE):
					if b1.x == b2.x and b1.y == b2.y + 1:
						b1.color = BLUE
						b2.color = BLUE
				elif b1.tab[1] == 1 and b2.tab[3] == 1 and (b1.color == BLUE or b2.color == BLUE):
					if b1.x+1 == b2.x and b1.y == b2.y:
						b1.color = BLUE
						b2.color = BLUE		


def draw():
	screen.fill(BLACK)
	for b in board:
		b.draw(n)
	screen.draw.filled_rect(Rect((S[0]*n,S[1]*n), (n, n)), BLUE)
	screen.draw.filled_rect(Rect((E[0]*n,E[1]*n), (n, n)), GREEN)



def on_mouse_down(pos, button):
	if button == mouse.LEFT:
		for b in board:
			if b.x*n<pos[0]<b.x*n+n and b.y*n<pos[1]<b.y*n+n:
				b.rotate()
	

	
S = [0,0]
E = [0,0]
board = []
X = 0
Y = 0
file=open("lvl.dat")
for line in file:
	X=0
	for s in line:
		if s == "1":
			board.append(Piece(X,Y,[1,1,1,1]))
		if s == "2":
			board.append(Piece(X,Y,[1,1,0,0]))
		if s == "3":
			board.append(Piece(X,Y,[1,0,1,0]))
		if s == "4":
			board.append(Piece(X,Y,[0,0,0,1]))
		if s == "5":
			board.append(Piece(X,Y,[1,1,1,0]))
		if s == "S":
			S = [X,Y]
			board.append(Piece(X,Y,[1,1,1,1]))
			board[-1].color = BLUE
		if s == "E":
			E = [X,Y]
			board.append(Piece(X,Y,[1,1,1,1]))
			board[-1].color = GREEN			
		for i in range(random.randint(0,3)):
			board[-1].rotate()
		
		X = X + 1
	Y = Y + 1
	
n = WIDTH//X




