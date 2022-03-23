# Path finding algorithms visualization tool
Python implementation of some pathfinding algorithms (A* search, Dijkstra, GreedyBFS) with GUI implemented using the **pygame module** to visualize what's going on. The algorithms are implemented using the **Manhattan distance** as heuristic and enabling only 4 type of movement (left,right,up,down).

Every file *'NameOfAlgorithm.py'* will start a pygame window with a 40x40 grid and:  
- By left clicking on the grid you can place the starting node (orange color), the goal node (blue color) and walls (black). 
- By right clicking you can clear the grid in specific spots.
- Once setted start, goal and (eventually) walls press **ENTER** to start the algorithm and the animation.
- Press **R** to reset everything and start a new grid.
- Press **M** to generate a random maze.
- Press **ESC** or close button to escape.
- Enjoy!

**Note:** since this project makes use of pygame and numpy modules, you should have them installed. You can do it by launching:

`pip install pygame numpy`
