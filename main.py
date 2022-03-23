import numpy as np
import pygame as pg
import os
import sys
from Algorithms.PathFinding import *

pg.init()
SCREEN = pg.display.set_mode((640,640))
WIDTH = 640//40   
NUM = 40
FPS = 30 # frames per second setting
fpsClock = pg.time.Clock()


class Node():

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    ORANGE = (255,153,51)
    CYAN = (153,255,255)
    GREEN = (128,255,0)
    BLUE =  (0,0,255)
    PINK = (204,153,255)

    def __init__(self, i, j, width, screen) -> None:

        self.row = i    
        self.col = j
        self.width = width
        self.screen = screen
        self.wall = False
        self.start = False
        self.goal = False
        self.color = self.WHITE
        
    def draw(self):
        """When called draws the node object on the screen based on its attributes by calling the draw.rect method."""
        rect = (self.col*self.width, self.row*self.width, self.width, self.width)
        pg.draw.rect(self.screen, color = self.color, rect=rect, width = 0)
        pg.draw.rect(self.screen, color = self.BLACK, rect=rect, width = 1)
        pg.display.update(rect)

    def make_start(self):
        self.color = self.ORANGE
        self.start = True
        self.draw()
    
    def make_goal(self):
        self.color = self.BLUE
        self.goal = True
        self.draw()

    def make_wall(self):
        self.color=self.BLACK
        self.wall = True
        self.draw()

    def make_explored(self):
        if self.start or self.goal:
            pass
        else:
            self.color = self.CYAN
            self.draw()

    def make_open(self):
        if self.start or self.goal:
            pass
        else:
            self.color = self.GREEN
            self.draw()


    def make_path(self):
        if self.start or self.goal:
            pass
        else:
            self.color = self.PINK
            self.draw()

    def reset(self):
        self.color = self.WHITE
        self.draw()
        
    
    def cost_to_move(self):

        return 1
        

def coordinate_map(x,y,rectwidth):
    """Function that maps the x,y coordinates of the screen to the actual node object in the map array. Returns i,j row and column indices."""
    i = y//rectwidth
    j = x//rectwidth

    return i,j

def make_map(screen, width, num):
    """Sets the map array and draws the grid on screen. Map is a numxnum array containing Node() objects in (row,col).
    Width is the side of the square. num is the number of rows and cols."""

    map = np.empty((num,num), dtype=object)
    start = None
    goal = None
    screen.fill((255,255,255))

    for i in range(num):
        for j in range(num):

            map[i,j] = Node(i,j,width, screen)
            pg.draw.rect(screen, color = (0,0,0), rect=(j*width, i*width, width, width), width = 1)

            if i == 0 or i == num-1 or j == 0 or j == num-1:
                map[i,j].make_wall()
    
    pg.display.update()

    return map,start,goal

def random_maze(screen,width, num):

    map,start,goal = make_map(screen,width,num)

    for i in range(1,num-1):
        for j in range(1,num-1):
            p = np.random.rand()
            if p < 0.2:
                map[i,j].make_wall()

    return map,start,goal


def drawPath(path,map):
    '''Draws the optimal path after the call of recover_path(). Path is the output of recover_path().'''
    
    for col,row in path:
        
        node = map[row,col]
        node.make_path()
        pg.time.wait(20)


def main(screen, width, num, A_star):
     
    map,start,goal = make_map(screen,width,num)
    run = True
    ended = False
    
    while run:
        for event in pg.event.get():

            while ended:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()

                    if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        sys.exit()

                    if event.type == pg.KEYDOWN and event.key == pg.K_r:
                        map,start,goal = make_map(screen,width,num) 
                        ended = False


            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                sys.exit()

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_RETURN and start!= None and goal!= None:

                    path = A_star(start,goal,map) 

                    if not path:
                        start = None
                        goal = None
                        ended = True

                    else:
                        
                        path = recover_path(start,goal,path)
                        drawPath(path,map)
                        start = None
                        goal = None
                        ended = True
                        
                elif event.key == pg.K_r:

                    map,start,goal = make_map(screen,width,num)
                
                elif event.key == pg.K_m:
                    map,start,goal = random_maze(screen,width,num)
                    

            if pg.mouse.get_pressed()[0]:
                    
                x,y = pg.mouse.get_pos()
                i,j = coordinate_map(x,y,WIDTH)
                node = map[i,j]
                
                if not start:
                    start = node
                    start.make_start()
                
                elif not goal and start!=node:
                    goal = node
                    goal.make_goal() 

                elif start!=node and goal!=node:
                    node.make_wall()
                
            elif pg.mouse.get_pressed()[2]:

                    x,y = pg.mouse.get_pos()
                    i,j = coordinate_map(x,y,WIDTH)
                    node = map[i,j]

                    if node.start:
                        
                        start = None
                        node.start = False

                    elif node.goal:

                        goal = None
                        node.goal = False

                    else:
                        node.wall = False

                    node.reset()

        pg.display.update()
        fpsClock.tick(FPS) 



if __name__ == '__main__':
    main(SCREEN, WIDTH, NUM, A_star)

