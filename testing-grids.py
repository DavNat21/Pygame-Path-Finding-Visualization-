import numpy as np
import pygame as pg
import os
import sys
import heapq

pg.init()
SCREEN = pg.display.set_mode((640,640))
WIDTH = 640//40
NUM = 40
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
    RED = (204,0,0)
    GREEN = (0,204,0)
    BLUE =  (0,0,255)
    PURPLE = (127,0,255)
    INITALIZE = True

    def __init__(self, i, j, width, height,screen) -> None:

        self.row = i    
        self.col = j
        self.width = width
        self.height = height
        self.screen = screen
        #self.neighbors = self.get_neighbors()
        self.wall = False
        self.start = False
        self.goal = False
        self.color = self.WHITE
        #self.cost = 1
        #self.set_wallstatus_onscreen()

    # def get_neighbors(self):
    #     """Return neighbors nodes objects"""
        
    #     x = self.col
    #     y = self.row
       
    #     if 0<=x< self.width and 0<=y< self.height:
    #         neighbors = [(x-1,y), (x+1,y), (x, y-1), (x,y+1)]
                    
    #         return neighbors
    #     else:
    #         return None
    
    def make_start(self):
        self.color = self.ORANGE
        self.start = True
    
    def make_goal(self):
        self.color = self.BLUE
        self.goal = True

    def make_wall(self):
        self.color=self.BLACK
        self.wall = True

    def make_explored(self):
        self.color = self.RED
        rect = (self.col*self.width, self.row*self.width, self.width, self.width)
        pg.draw.rect(self.screen, color = self.color, rect=rect, width = 0)
        pg.display.update(rect)

    def make_open(self):
        self.color = self.GREEN
        rect = (self.col*self.width, self.row*self.width, self.width, self.width)
        pg.draw.rect(self.screen, color = self.color, rect=rect, width = 0)
        pg.display.update(rect)


    def make_path(self):
        self.color = self.PURPLE
        rect = (self.col*self.width, self.row*self.width, self.width, self.width)
        pg.draw.rect(self.screen, color = self.color, rect=rect, width = 0)
        pg.display.update(rect)


    def initialize_on_grid(self):
        self.color = self.WHITE
        rect = (self.col*self.width, self.row*self.width, self.width, self.width)
        pg.draw.rect(self.screen, color = self.WHITE, rect=rect, width = 0)
        pg.draw.rect(self.screen, color = self.BLACK, rect=rect, width = 1)
    
    def cost_to_move(self):

        return 1

    # def set_wallstatus_onscreen(self):
        
    #     w = self.width
    #     x = self.col
    #     y = self.row


    #     if self.INITALIZE:

    #         pg.draw.rect(self.screen, color = self.BLACK, rect=(x*w, y*w, w, w), width=1)
    #         self.INITALIZE = False
        
    #     elif self.start:
    #         pg.draw.rect(self.screen, color = self.ORANGE, rect=(x*w, y*w, w, w))
        
    #     elif self.goal:

    #         pg.draw.rect(self.screen, color = self.BLUE, rect=(x*w, y*w, w, w))

    #     elif self.wall:
            
    #         pg.draw.rect(self.screen, color = self.BLACK, rect=(x*w, y*w, w, w))
        
    #     else:
    #         pg.draw.rect(self.screen, color = self.WHITE, rect=(x*w, y*w, w, w), width=0)
    #         pg.draw.rect(self.screen, color = self.BLACK, rect=(x*w, y*w, w, w), width=1)

def get_neighbors(node,width,map):
        """Return neighbors nodes objects"""
        
        x,y = node.col,node.row
        support = []
       
        if 0<=x<width and 0<=y< width:

            neighbors = [map[y,x-1], map[y,x+1], map[y-1,x], map[y+1,x]]

            for node in neighbors:
                if not node.wall:
                    support.append((node.col,node.row))

            return support
        else:
            return None

def update_grid(screen, node) -> Node:
    """when called draws and update the actual grid state"""
    
    x = node.col
    y = node.row
    w = node.width
    pg.draw.rect(screen, color = node.color, rect=(x*w, y*w, w, w))
    #pg.display.update()



def heuristic(current, goal):
    """Manhattan distance"""
    x,y = current.col, current.row
    x2,y2 = goal.col, goal.row

    return abs(x-x2) + abs(y-y2)

def coordinate_map(x,y,rectwidth):
    i = y//rectwidth
    j = x//rectwidth

    return i,j

def make_map(screen, width, num):
    """note: for now assuming working with 640x640 screen and 20x20 grid"""

    map = np.empty((num,num), dtype=object)

    for i in range(num):
        for j in range(num):

            map[i,j] = Node(i,j,width, width, screen)
            pg.draw.rect(screen, color = (0,0,0), rect=(j*width, i*width, width, width), width = 1)
    return map

class PriorityQueue():
    """implemento una priority queue utilizzando il modulo heapq di python. 
        Inizializzo una lista vuota e definisco i due metodi push e pop"""

    def __init__(self):

        self.queue = []

    def is_empty(self):
        """By default python considera le liste True a meno che non siano vuote...cosa strana ma è cosi."""
        return not self.queue

    def heap_push(self, item, priority):

        heapq.heappush(self.queue, (priority, item))
    
    def pop(self):

        return heapq.heappop(self.queue)[1]




def drawPath(path,map):
    '''funzione per disegnare il percorso individuato: cambia il valore dei pixel in base a color creando una retta dal punto (x0,y0) al punto (x1,y1)'''
    
    for col,row in path:
        
        node = map[row,col]
        node.make_path()

        

def recover_path(start, goal, explored):
    """Explored is a dictionary {child(x,y):parent(x,y)} """
    
    current = (goal.col,goal.row)
    path = []

    while (current[0] != start.col) or (current[1] != start.row):

        path.append(explored[current])
        current = explored[current]

    path.append((start.col,start.row))
    path.reverse()

    return path

def A_star(start, goal, map):

    #default_cost = (abs(start[0]-goal[0]) + abs(start[1]-goal[1]))/graph.scaling
    s = (start.col, start.row)
    g = (goal.col, goal.row)
    to_explore = PriorityQueue()
    to_explore.heap_push(s, 0)  #pusho lo starting point
    explored = {}
    explored[s] = 0            #dizionario contenente pair nodo:costo per raggiungerlo dallo start
    path = {}                      #dizionario contenente pair nodo:nodo_da_cui_arrivo


    while not to_explore.is_empty():

        a,b = current = to_explore.pop()
        map[b,a].make_explored()

        if current == g:
            
            break

        for x,y in get_neighbors(map[current[1],current[0]],640,map):

            node = map[y,x]
            cost = explored[current] + node.cost_to_move()

            if (x,y) not in explored.keys() or cost < explored[(x,y)]:

                priority = cost + heuristic(node, goal)       # aggiungo l'euristica come criterio di priorità
                explored[(x,y)] = cost
                to_explore.heap_push((x,y), priority)
                path[(x, y)] = current
                node.make_open()
        pg.time.wait(40)
    if current!=g:
        return []  #an empty path

    return path




def main(screen, width,num):
    
    screen.fill((255,255,255))  #fill screen with white background
    
    map = make_map(screen,width,num)

    start = None
    goal = None
    run = True
    started = False
    pg.display.update()
    
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if started:
                continue

            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_RETURN and start!= None and goal!= None:
                    
                    started = True
                    path = A_star(start,goal,map)

                    if not path:
                        started = False

                        continue
                    else:
                        
                        path = recover_path(start,goal,path)
                        print('ok ho svolto l algoritmo')
                        drawPath(path,map)
                        start = None
                        goal = None

                


             
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
            
            update_grid(screen, node)

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

                node.initialize_on_grid()

                
        #start is None
        #goal is None
        #pg.time.delay(100) 
        pg.display.update() 



main(SCREEN, WIDTH, NUM)