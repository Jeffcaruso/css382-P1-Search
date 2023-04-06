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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #fringe holding potential options
    fringe = util.Stack()

    #set of visited places
    visited = []
    
    #coordinates positions
    confi = problem.getStartState()
    
    #building and placing starting location on the fringe
    initialState = (confi,[],0)
    fringe.push(initialState)
    
    while not fringe.isEmpty():      
        #get top of fringe  
        state, path, cost = fringe.pop()
        if(problem.isGoalState(state)):
            #reached destination, return path
            return path
            
        #optain possible options where it can go 
        options = problem.getSuccessors(state)
        #mark state as visited (one that says where we can go)
        visited.append(state) 
        
        for child, action, cost in options:
            #for each possible direction (options)
            if child not in visited:   
                #if coordinates (child) aren't visited             
                testing = (child, path + [action] , cost)
                #save
                fringe.push(testing)
    #end of DFS
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #fringe holding potential options
    fringe = util.Queue()

    #set of visited places
    visited = []
    
    #coordinates positions
    confi = problem.getStartState()
    
    #building and placing starting location on the fringe
    initialState = (confi,[],0)
    fringe.push(initialState)
    
    while not fringe.isEmpty():      
        #get top of fringe  
        state, path, cost = fringe.pop()
        if(problem.isGoalState(state)):
            #reached destination, return path
            return path
            
        #optain possible options where it can go 
        options = problem.getSuccessors(state)
        #mark state as visited (one that says where we can go)
        visited.append(state) 
        
        for child, action, cost in options:
            #for each possible direction (options)
            if child not in visited:   
                #if coordinates (child) aren't visited             
                testing = (child, path + [action] , cost)
                #save
                fringe.push(testing)
    #end of DFS

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #fringe holding potential options
    fringe = util.PriorityQueue()

    #set of visited places
    visited = []
    
    #coordinates positions
    confi = problem.getStartState()
    
    #building and placing starting location on the fringe
    initialState = (confi,[],0)
    fringe.push(initialState, 0)
    
    while not fringe.isEmpty():      
        #get top of fringe  
        state, path, cost = fringe.pop()
        if(problem.isGoalState(state)):
            #reached destination, return path
            return path
            
        #optain possible options where it can go 
        options = problem.getSuccessors(state)
        #mark state as visited (one that says where we can go)
        visited.append(state) 
        
        for child, action, cost in options:
            #for each possible direction (options)
            if child not in visited:   
                #if coordinates (child) aren't visited             
                testing = (child, path + [action] , cost)
                #save
                fringe.push(testing,cost)
    
    #end of UCS   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #fringe holding potential options
    fringe = util.PriorityQueue()

    #set of visited places
    visited = []
    
    #coordinates positions
    confi = problem.getStartState()
    
    #building and placing starting location on the fringe
    initialState = (confi,[],0)
    fringe.push(initialState, 0)
    
    while not fringe.isEmpty():      
        #get top of fringe  
        state, path, cost = fringe.pop()
        #print(heuristic)
        if(problem.isGoalState(state)):
            #reached destination, return path
            return path
            
        #optain possible options where it can go 
        options = problem.getSuccessors(state)
        #mark state as visited (one that says where we can go)
        visited.append(state) 
        
        for child, action, cost in options:
            #for each possible direction (options)
            if child not in visited:   
                #if coordinates (child) aren't visited
                # import manhattanHeuristic from searchAgents
                # from searchAgents import manhattanHeuristic

                #h = 1
                #hCost = manhattanHeuristic(child, problem)
                print(heuristic)
                #hCost = getHeuristicCost(child,problem, heuristic)
                hCost = heuristic(child,problem)
                #cost += test
                testing = (child, path + [action] , cost) #cost + test? 
                #but then cost has previous?
                #save
                fringe.push(testing,cost + hCost)
    
    #end of AStar   

# def getHeuristicCost(child, problem, heuristic):
#     from searchAgents import manhattanHeuristic,euclideanHeuristic,cornersHeuristic
#     Hcost = 1
#     print(heuristic)
#     if heuristic == "manhattanHeuristic":
#         Hcost = manhattanHeuristic(child,problem)
#         print(Hcost)
#     elif heuristic == "euclideanHeuristic":
#         Hcost = euclideanHeuristic(child,problem)
#     elif heuristic == "cornersHeuristic":
#         Hcost = cornersHeuristic(child,problem)
#
#     #print(Hcost)
#     return Hcost


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
