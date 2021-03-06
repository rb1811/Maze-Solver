from imp import reload
import pygame
from play import playtile
import graphics
import database
i=1;
emaze=[];
sch=input("1.want to enter maze\n2.to solve inbuilt maze:")
if(sch==2):
	database.inbuiltmaze()	
	grid=database.grid
elif(sch==1):
	for x in range(0,4):
		a=input('enter the row of the maze in decimal format')
		emaze.append(a)
	emaze.append(33);
	print("the entered maze in decimal format is with destination at the end \n")
	print emaze;
	database.usermaze(emaze)
	grid=emaze
schoice=input("ENTER \n1.DFS solution \n2.BFS solution\n3.Self Solve\n:")
if(schoice == 1):
	grid =database.grid
	grid[database.xx][database.yy]=2
	graphics.mazedisplay(grid,1,-1)
	def search(x, y):
		    if grid[x][y] == 2:
		        print 'found at %d,%d' % (x, y)
			graphics.dest(x,y)        
			return True
		    elif grid[x][y] == 1:
		        print 'wall at %d,%d' % (x, y)
		        playtile("wall")
		        return False
		    elif grid[x][y] == 3:
		        print 'visited at %d,%d' % (x, y)
			return False
	     
		    print 'visiting %d,%d' % (x, y)
		    a=str(x)+str(y)
		    graphics.path(x,y)
		    playtile(a)
		    grid[x][y] = 3
		    graphics.visit(x,y)
		 
		    if ((x < len(grid)-1 and search(x+1, y))
		        or (y > 0 and search(x, y-1))
		        or (x > 0 and search(x-1, y))
		        or (y < len(grid)-1 and search(x, y+1))):
		        return True
	
		    return False		 
	search(0,0)	
elif(schoice==2):
	import bfsmaze
	bfsmaze.bfssolution(grid,database.start,database.dest,database.choice)
	ans=bfsmaze.ans
	graphics.mazedisplay(grid,2,database.dest)
	for x in range(len(ans)):
		ans[x]=int(ans[x])
		a=str(ans[x]%10)+str(ans[x]/10)
		graphics.path(ans[x]%10,ans[x]/10)
		playtile(a)
		graphics.visit(ans[x]%10,ans[x]/10)
		if(ans[x]==database.dest):
			graphics.dest(ans[x]%10,ans[x]/10)
if(schoice==3):
	x,y=10,10
	grid =database.grid
	grid[database.xx][database.yy]=2
	graphics.mazedisplay(grid,1,-1)
	screen=graphics.screen
	red=graphics.red
	pygame.draw.circle(screen, red, (x,y), 7, 0);
	pygame.display.update()
	wall=(0,0,0,255)
	boundary=(0,255,0,255)
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pixelcolor=screen.get_at((x-15,y))
					if(pixelcolor!=wall and pixelcolor!=boundary):
						x=x-15
						graphics.mazedisplay(grid,1,-1)
						pygame.draw.circle(screen, red, (x,y), 7, 0); 
						pygame.display.update()               
				elif event.key == pygame.K_RIGHT:
					pixelcolor=screen.get_at((x+15,y))
					if(pixelcolor!=wall and pixelcolor!=boundary):
						x=x+15
						graphics.mazedisplay(grid,1,-1)
						pygame.draw.circle(screen, red, (x,y), 7, 0); 
						pygame.display.update()
				elif event.key == pygame.K_UP:
					pixelcolor=screen.get_at((x,y-15))
					if(pixelcolor!=wall and pixelcolor!=boundary):
						y=y-15
						graphics.mazedisplay(grid,1,-1)
						pygame.draw.circle(screen, red, (x,y), 7, 0); 
						pygame.display.update()                
				elif event.key == pygame.K_DOWN:
					pixelcolor=screen.get_at((x,y+15))
					if(pixelcolor!=wall and pixelcolor!=boundary):
						y=y+15
						graphics.mazedisplay(grid,1,-1)
						pygame.draw.circle(screen, red, (x,y), 7, 0); 
						pygame.display.update()
