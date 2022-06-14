# PacmanSearch using Breadth/Depth First Search Algorithm
![bfs pacman](https://user-images.githubusercontent.com/60335543/173474584-f35df935-3b1f-4acc-940c-3a1abbf99603.png)
<br>***Pacman exploring a maze using Breadth First Search*** <br><br>
![dfs pacman](https://user-images.githubusercontent.com/60335543/173474601-44b50bfd-d055-4fc4-b5b2-9369c570cbe9.png)
<br>***Pacman exploring a maze using Depth First Search***

---
Code framework provided by [**UC Berkeley CS188 Intro to AI**](http://ai.berkeley.edu/project_overview.html). <br><br>
Program project required implementation of searching/graphing algorithm; specifically, Depth First Search and Breadth First Search. Most edits made to the framework can be found in the files: search.py and pacman.py. 



## Installation
- Python 2.7 is required to run this program.
- pip and virtualenv must be installed.
- Create virtual environment with the command **virtualenv (name)** --> (personally, I did: **virtualenv pacpac**. Feel free to use the same)
- Download the directory, open terminal in root folder.
- Enter in commandline: **source (name)/bin/activate** --> or **source pacpac/bin/activate** (if you are following what I have done)
- Navigate to the *pacman* directory by **cd code --> cd pacman**
- Run the command: **python pacman.py** (install required packages if asked.)

## Goal of Project
- Implement Depth First and Breadth First Search algorithms using the framework provided.
- Eliminate redundant commandline typing to effectively provide better visual comparisons for the algorithms.
- Implement simple user menu. Allowing user to repeatedly load up classic pacman or pacman with search algorithms.
- Menu will allow User to select between the different provided mazes for Pacman to search through or play on.

## How it Works
**Background Information on Search Algorithms**
- Breadth First Search is a searching algorithm that will explore a Node and all of it's adjacent neighbors until it finds the the goal. This can be better visualized as a Tree structure. Starting at the root node, the algorithm will search all children nodes and mark each node as *visited* until it finds the target node.
- Depth First Search will search from the root node and search along the path of a child node until it reaches a node with no child. The algorithm will backtrack along the path and search for nodes with unvisited children and mark them visited. Then, it will backtrack to the root node and search along the path of the next unvisited child node.
- Data structures used were Stack and Queue. 
- More information on [Depth First Search](https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/depth-first-search-dfs-algorithm/) along with visuals and code implementation.
- More information on [Breadth First Search](https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/breadth-first-search-bfs-algorithm/) along with visuals and code implementation.
- *Note: Depth First search can be implemented recursively. A stack was used for this search algorithm*

**Background Information on Framework**
- Each instance of a Pacman game has pacman in a randomized location
- Different sized mazes for pacman to explore. Maps consist of tinyMaze, mediumMaze, and bigMaze.
- To see original [code](http://ai.berkeley.edu/project_overview.html), visit the link.
- To run original code there may be other steps required when running through command line. 
- The framework provides a variety of options to tweak with pacman game. For example, choosing amount of ghosts, different map, how long the game runs, etc.
- To enter pacman game with different options, more is required when running the code through commandline.

**Using the Framework**
- Using helper functions provided by the framework, it was possible to get a tuple containing the coordinate, direction, and cost of the action(for pacman).
- Helper functions used in this project include; problem.isGoalState, problem.getStartState, and problem.getSuccessors.
- Using problem.getSuccessors, it was possible to get a list of all adjacent nodes along with the tuple containing the coordinates, direction, and cost.
- With these functions, implementation of the two search algorithms was doable because of the provided information.

### ***Author Notes:***
- There is always room for improvement for this project, in terms of code optimization, user experience, and user interface.
- The main goal of this project was to implement the search algorithms. Everything else was implemented solely because the Author desired so.
- Intended end goal/vision for this project is to create an authentic user experience and GUI. 


