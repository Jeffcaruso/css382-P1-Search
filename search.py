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
                node = (child, path + [action] , cost)
                #save
                fringe.push(node)
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
            return path
            
        #optain possible options where it can go 
        if state not in visited:
            options = problem.getSuccessors(state)
            visited.append(state) 
        else:
            options = []
        #mark state as visited (one that says where we can go)
        
        for child, action, cost in options:
            #for each possible direction (options)
            if child not in visited:   
                #if coordinates (child) aren't visited             
                node = (child, path + [action] , cost)
                #save
                fringe.push(node)
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
        state, path, TrueCost = fringe.pop()
        #print("my output popping",state, path, TrueCost)

        if(problem.isGoalState(state)):
            #reached destination, return path
            return path
       
        #obtain possible options where it can go 
        if state not in visited:
            options = problem.getSuccessors(state)
            visited.append(state)  #state?
        else:
            options = []
        
        for child, action, cost in options:
            #print("my output pushing",child, path + [action], cost + TrueCost)
            node = (child, path + [action] ,cost + TrueCost) #cost
            #save
            fringe.push(node, TrueCost + cost)
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
    initialConfig = problem.getStartState()
    
    #building and placing starting location on the fringe
    initialState = (initialConfig,[],0)
    fringe.push(initialState, 0)
    
    while not fringe.isEmpty():      
        #get top of fringe  
        state, path, TrueCost = fringe.pop()

        if(problem.isGoalState(state)):
            #reached destination, return path
            return path
            
        #optain possible options where it can go 
        if state not in visited:
            options = problem.getSuccessors(state)
            visited.append(state)  #state?
        else:
            #is visited, so don't do anything with it, 
            #    for loop does nothing b/c no options exist...
            options = []

        for child, action, cost in options:
            #for each possible direction (options)  
            hCost = heuristic(child,problem)
            node = (child, path + [action] , TrueCost + cost)
            #True cost = cost from fringe from before...
            fringe.push(node, TrueCost + cost + hCost)
    #end of AStar   


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
