# A-search-visualization-tool
A python implementation of A* search algorithm with GUI implemented using the **pygame module** to visualize what's going on. The algorithm is implemented using the Manhattan distance as heuristic and enabling only (left,right,up,down) movement (for now). In that way A* will be correct and optimal.

The main() will start a window with a 40x40 grid and:  
- By left clicking on the grid you can place the starting node (orange color), the goal node (blue color) and walls (black). 
- By right clicking you can clear the grid in specific spots.
- Once setted start, goal and (eventually) walls press ENTER to start the algorithm and the animation.
- Press R to reset everything and start a new grid.
- Press esc or close button to escape.
- Enjoy!

**Note:** since this makes heavy use of pygame module, you should have it installed. You can do it by launching:

`pip install pygame`
