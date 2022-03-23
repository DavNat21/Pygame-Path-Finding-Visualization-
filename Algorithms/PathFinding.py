# Path finding algorithms implementation for the pygame project. Here's a list of the available:
# A* search
# Dijkstra
# Greedy Best First Search


import heapq
import pygame as pg

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

def get_neighbors(node,screenside,map):
        """Return a list of neighbor's (row,col). If a node is a wall, then is not included in the neighbors. 
           If no neighbors are found, returns None."""
        
        x,y = node.col,node.row
        support = []
       
        if 0<=x<screenside and 0<=y< screenside:

            neighbors = [map[y,x-1], map[y,x+1], map[y-1,x], map[y+1,x]]

            for node in neighbors:
                if not node.wall:
                    support.append((node.col,node.row))

            return support
        else:
            return None

def heuristic(current, goal):
    """Manhattan distance"""
    x,y = current.col, current.row
    x2,y2 = goal.col, goal.row

    return abs(x-x2) + abs(y-y2)

###############################################################################################################
###############################################################################################################
####################################### Path finding algorithms #################################################
###############################################################################################################
###############################################################################################################


def A_star(start, goal, map):
    """A star algorithm implementation."""

    s = (start.col, start.row)
    g = (goal.col, goal.row)
    to_explore = PriorityQueue()
    to_explore.heap_push(s, 0)  
    explored = {}
    explored[s] = 0            
    path = {}                      


    while not to_explore.is_empty():

        a,b = to_explore.pop()
        map[b,a].make_explored()

        if (a,b) == g:
            
            break

        for x,y in get_neighbors(map[b,a],640,map):

            node = map[y,x]
            cost = explored[(a,b)] + node.cost_to_move()

            if (x,y) not in explored.keys() or cost < explored[(x,y)]:

                priority = cost + heuristic(node, goal)    
                explored[(x,y)] = cost
                to_explore.heap_push((x,y), priority)
                path[(x, y)] = (a,b)
                node.make_open()
        pg.time.wait(20)

    if (a,b)!=g:
        return []  #an empty path

    return path

def Dijkstra(start, goal, map):
    """Dijkstra's algorithm implementation."""

    s = (start.col, start.row)
    g = (goal.col, goal.row)
    to_explore = PriorityQueue()
    to_explore.heap_push(s, 0)  
    explored = {}
    explored[s] = 0            
    path = {}                      


    while not to_explore.is_empty():

        a,b = to_explore.pop()
        map[b,a].make_explored()

        if (a,b) == g:
            
            break

        for x,y in get_neighbors(map[b,a],640,map):

            node = map[y,x]
            cost = explored[(a,b)] + node.cost_to_move()

            if (x,y) not in explored.keys() or cost < explored[(x,y)]:

                priority = cost     
                explored[(x,y)] = cost
                to_explore.heap_push((x,y), priority)
                path[(x, y)] = (a,b)
                node.make_open()
        pg.time.wait(20)

    if (a,b)!=g:
        return []  #an empty path



def GreedyBFS(start, goal, map):
    """GreedyBFS algorithm implementation."""

    s = (start.col, start.row)
    g = (goal.col, goal.row)
    to_explore = PriorityQueue()
    to_explore.heap_push(s, 0)  
    explored = {}
    explored[s] = 0            
    path = {}                      


    while not to_explore.is_empty():

        a,b = to_explore.pop()
        map[b,a].make_explored()

        if (a,b) == g:
            
            break

        for x,y in get_neighbors(map[b,a],640,map):

            node = map[y,x]
            cost = explored[(a,b)] + node.cost_to_move()

            if (x,y) not in explored.keys() or cost < explored[(x,y)]:

                priority = heuristic(map[b,a], goal)     
                explored[(x,y)] = cost
                to_explore.heap_push((x,y), priority)
                path[(x, y)] = (a,b)
                node.make_open()
        pg.time.wait(20)

    if (a,b)!=g:
        return []  #an empty path

    return path




def recover_path(start, goal, explored):
    """Function used to recover the path after A_star is called. Note: Explored should be a dictionary {child(x,y):parent(x,y)}
        and it's the output of algorithms function. """
    
    x,y = (goal.col,goal.row)
    path = []

    while (x != start.col) or (y != start.row):

        path.append(explored[(x,y)])
        x,y = explored[(x,y)]

    path.append((start.col,start.row))
    path.reverse()

    return path