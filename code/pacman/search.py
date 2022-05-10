# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def convert2vertex(state, corner = False):
    if corner:
        return state[0][0] * 1000 * 16 + state[0][1] * 16 + state[1]
    else:
        return state[0] * 1000 + state[1]

def convert2state(value, corner = False):
    if corner:
        status = value % 16
        y = ((value - status) // 16) % 1000
        x = value // (1000 * 16)
        return ((x, y), status)
    else:
        x = value // 1000
        y = value % 1000
        return (x, y)

def breadthfirstSearch(problem):
    # #defining the initial state in a tuple with problem.getStartState() & cost
    # node = { 'state': problem.getStartState(), 'cost': 0 }

    # #if our start state is is the goal then we return
    # if problem.isGoalState(node['state']):
    #     return []
    
    # #creating a queue for bfs
    # battleground = util.Queue()
    # battleground.push(node)

    # explored = set()
    # actions = []
    # while True:
    #     if battleground.isEmpty():
    #         raise Exception('Search failed')

    #     node = battleground.pop()

    #     explored.add(node['state'])
    #     #problem.getSuccessors will get a list of nodes with the coordinate, direction, and cost
    #     successors = problem.getSuccessors(node['state'])
    #     #we iterate through the list of child nodes and define child with a tuple containing node info
    #     for successor in successors:
    #         child = { 'state': successor[0], 'action': successor[1], 'cost': successor[2], 'parent': node }
    #         #while exploring, if a child node happens to be the goal; then, we need to backtrack
    #         # and return a list of actions(directions) we took to get there. We can backtrack through
    #         # the 'parent of our child tuple
    #         if child['state'] not in explored:
    #             actions.append(child['action'])
    #             if problem.isGoalState(child['state']):
    #                 print("goal found.")
                    
    #                 node = child
                    
    #                 #actions.reverse() #probably a good idea
    #                 print(actions)
    #                 #reached goal return the list of actions
    #                 return actions
    #             battleground.push(child)
    
    #initializations
    explored = {}
    path = []
    solution = []
    queue = util.Queue()
    parents = {}

    #problem.getSuccessors will get a list of nodes with the coordinate, direction, and cost
    start = problem.getStartState()
    queue.push((start, 'Undefined', 0))
    explored[start] = 'Undefined'

    if problem.isGoalState(start):
        return solution

    goal = False
    while(goal != True):
        if queue.isEmpty():
            raise Exception('Search Failed')
        node = queue.pop()
        #using dictionary to store node coords with direction to get there
        explored[node[0]] = node[1]

        if problem.isGoalState(node[0]):
            node_sol = node[0]
            goal = True
            break
        
        #expand node and look through successors/child
        for elem in problem.getSuccessors(node[0]):
            if elem[0] not in explored.keys() and elem[0] not in parents.keys():
                #loop through each child of start node and assign child nodes = start.coords. Continue looping as long as it is not explroed
                parents[elem[0]] = node[0]
                queue.push(elem)
                
        
    while(node_sol in parents.keys()):
        #finding parent node of solution node
        node_sol_prev = parents[node_sol]
        solution.insert(0, explored[node_sol])
        node_sol = node_sol_prev

    return solution


def depthfirstSearch(problem):
#using a stack instead of recursion
    
    #initializations
    explored = {}
    solution = []
    stack = util.Stack()
    parents = {}

    start = problem.getStartState()
    stack.push((start, 'Undefined', 0))
    
    explored[start] = 'Undefined'

    if problem.isGoalState(start):
        return solution
    
    goal = False
    while (goal != True):
        if stack.isEmpty():
            raise Exception('Search failed')
        
        node = stack.pop()

        explored[node[0]] = node[1]

        if problem.isGoalState(node[0]):
            node_sol = node[0]
            goal = True
            break

        #expand nodes
        for elem in problem.getSuccessors(node[0]):
            if elem[0] not in explored.keys():
                parents[elem[0]] = node[0] #node is start or parent further into loop. elem is child nodes
                stack.push(elem)

    while(node_sol in parents.keys()):
        node_sol_prev = parents[node_sol]
        solution.insert(0, explored[node_sol]) #giving direction for solution

        node_sol = node_sol_prev
    return solution


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    from minheap import MinHeap

    heap = MinHeap()

    prev = {}
    dist = {}
    visited = {}

    startState = problem.getStartState()
    corner = True if isinstance(startState[0], tuple) else False

    vertex = convert2vertex(startState, corner)
    dist[vertex] = 0
    prev[vertex] = (None, None)

    heap.push(vertex, 0)

    while True:
        vertex, distance = heap.top()
        heap.pop()
        if (dist[vertex] != distance):
            continue
        visited[vertex] = True

        currentState = convert2state(vertex, corner)
        if problem.isGoalState(currentState):
            break

        for nextState, action, cost in problem.getSuccessors(currentState):
            nextVertex = convert2vertex(nextState, corner)
            if nextVertex in visited:
                continue

            if nextVertex not in dist:
                dist[nextVertex] = 9999999

            if (distance + cost < dist[nextVertex]):
                dist[nextVertex] = distance + cost
                heap.push(nextVertex, dist[nextVertex])
                prev[nextVertex] = (action, vertex)

    path = []
    vertex = convert2vertex(currentState, corner)
    current = prev[vertex]
    while (current[0] != None):
        path = [current[0]] + path
        current = prev[current[1]]

    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



# Abbreviations
ucs = uniformCostSearch
bfs = breadthfirstSearch #added in function to be called from cli
dfs = depthfirstSearch
