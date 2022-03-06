import numpy as np
import pygame as pg
import os
import sys

pg.init()

#pg.draw.rect(screen, color = (255,255,255), rect=(0,0,20,20))
#pg.display.update()
  

# def make_grid():
#     """make a 2d grid (it works)"""
#     x = 0
#     y = 0
#     for i in range(640//20):

#         y = i*20

#         for j in range(640//20):

#             x = j*20 
#             pg.draw.rect(screen, color= (0,0,0), rect =(x,y,20,20), width=1)
#     pg.display.update()

# make_grid()


class Node():

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    ORANGE = (255,128,0)
    PURPLE = (127,0,255)
    INITALIZE = True

    def __init__(self, i, j, width, height,screen) -> None:

        self.row = i    
        self.col = j
        self.width = width
        self.height = height
        self.screen = screen
        self.neighbors = self.neighbors()
        self.wall = False
        self.start = False
        self.goal = False
        self.color = self.WHITE
        self.set_status_onscreen()

    def neighbors(self):
        """Return neighbors nodes objects"""
        
        x = self.col
        y = self.row
       
        if 0<=x< self.width and 0<=y< self.height:
            neighbors = [(x-1,y), (x+1,y), (x, y-1), (x,y+1)]
                    
            return neighbors
        else:
            return None
    
    def set_status_onscreen(self):
        
        w = self.width
        x = self.col
        y = self.row

        if self.wall:
            
            pg.draw.rect(self.screen, color = (0,0,0), rect=(x*w, y*w, w, w))
        elif self.INITALIZE:

            pg.draw.rect(self.screen, color = (0,0,0), rect=(x*w, y*w, w, w), width=1)
            self.INITALIZE = False
        else:
            pg.draw.rect(self.screen, color = (255,255,255), rect=(x*w, y*w, w, w), width=0)
            pg.draw.rect(self.screen, color = (0,0,0), rect=(x*w, y*w, w, w), width=1)





def heuristic(x,y, goal):
    """Manhattan distance"""
    x2,y2 = goal

    return abs(x-x2) + abs(y-y2)

def coordinate_map(x,y,rectwidth):
    i = y//rectwidth
    j = x//rectwidth

    return i,j

def make_map(screen):
    """assuming working with 640x640 screen and 40x40"""
    map = np.empty((20,20), dtype=object)
    width = 640//20

    for i in range(20):
        for j in range(20):

            map[i,j] = Node(i,j,width, width, screen)
            #pg.draw.rect(screen, color = (0,0,0), rect=(j*width, i*width, width, width))
    return map

def main():

    
    screen = pg.display.set_mode((640,640))

    screen.fill((255,255,255))
    
    map = make_map(screen)

    pg.display.update()

    pos = 0


    while True:
        for event in pg.event.get():
            if event.type in (pg.QUIT, pg.KEYDOWN):
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                
                x,y = event.pos
                i,j = coordinate_map(x,y,640//20)

                if not map[i,j].wall:
                    map[i,j].wall = True
                    map[i,j].set_status_onscreen()
                else:
                    map[i,j].wall = False
                    map[i,j].set_status_onscreen()

        #pg.time.delay(100) 
        pg.display.update() 



main()