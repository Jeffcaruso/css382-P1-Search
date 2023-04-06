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

    fringe = util.Stack() #intalize stack (probably holding successors)
    actions = [] #store path of actions done to get to goal
    #maybe we'll need to keep pervious nodes? visted 
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    "Order for direction selection N, E, S, W"
    'problem.g'

    ## So, in the end, we will need to be constructing this.
    # So we will ask where can we go,
    # is it not visited yet?
    # go there, update items, add directions to the list.
    # initial testing
    #set the intial state
    #set intial position 

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    #making a agent 'pointer
    from game import GameStateData
    

    from game import Configuration
    from game import Actions
    # import game
    # localConfig = game.Configuration()
    #Configuration localConfig = Configuration()

    # #step 1 build directions
    # # South
    # a = 0
    # b = -1
    # vectorS = a,b
    # # North
    # a = 0
    # b = -1
    # vectorN = a,b
    # # East
    # a = 1
    # b = 0
    # vectorE = a,b

    # # West
    # a = -1
    # b = 0
    # vectorW= a,b

    # visited = [(5,5)]

    # #stack is 'fringe'
    # #push the start of the stack  (starting position) (push starting configuration)
    # #act = Actions.vectorToDirection(vectorS) #WorkOnLater()
    
    # ###probably need to do something here like pushing on the first round of items
    # act = None
    # startState = problem.getStartState() #starting state 
    # localCon = Configuration(startState, act) #WorkOnLater (dynamic config start location)
    # # get possible paths
    # options = problem.getSuccessors(localCon.getPosition()) # [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    
    # for coor,dir,cost in options:
    #     print("in for loop ",coor, dir, cost)
    #     localCon = Configuration(coor , dir)
    #     if (visited.__contains__(localCon.getPosition())):
    #         print("already visited") # shouldn't hit this...
    #     else:
    #         #push onto stack
    #         # visited.append(localCon.getPosition())
    #         print(localCon.direction)
    #         fringe.push(localCon)            
    #     #end of for loop

    # visited.append(startState)
    # localCon = fringe.pop()
    # visited.append(localCon.getPosition())
    # actions.append(localCon.getDirection()) 
    # if problem.isGoalState(localCon.getPosition()): # if the intial state is the goal state 
    #     return actions 
    
    # for coor,dir,cost in options:
    #     print("in for loop ",coor, dir, cost)
    #     localCon = Configuration(coor , dir)
    #     if (visited.__contains__(localCon.getPosition())):
    #         print("already visited")
    #         actions.pop() 
    #         #actions.remove()
    #     else:
    #         #push onto stack
    #         # visited.append(localCon.getPosition())
    #         fringe.push(localCon)



    

    # #print(fringe.pop())
    # #print(fringe.pop())
    # print("before starting while loop")

    # #fringe.push(localCon) # pushing on starting position
    # #move from that...
    # while not fringe.isEmpty():    ##somewhere near the start, need to check if we have left the destination
    #     localCon = fringe.pop()
    #     print(localCon.getPosition())
    #     #if checks if its been visited 
    #         # add position to visited  if has not been visited 
    #     visited.append(localCon.getPosition())
    #     actions.append(localCon.getDirection()) #change this to add
    #     if problem.isGoalState(localCon.getPosition()):
    #         print(actions)
    #         return actions 
            
    #     import time
    #     time.sleep(1)
    #     # get possible paths
    #     options = problem.getSuccessors(localCon.getPosition()) # [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    #     print("options:", problem.getSuccessors(localCon.getPosition()))
        
    #     for coor,dir,cost in options:
    #         print("in for loop ",coor, dir, cost)
    #         localCon = Configuration(coor , dir)
    #         if (visited.__contains__(localCon.getPosition())):
    #             print("already visited")
    #             actions.pop() 
    #             #actions.remove()
    #         else:
    #             #push onto stack
    #             # visited.append(localCon.getPosition())
    #             fringe.push(localCon)
            
    #         #end of for loop
    
    

    """
    act = Actions.vectorToDirection(vectorS)

    print(act)

    localCon = Configuration((5,5), act)

    print(localCon.getPosition())

    localCon = localCon.generateSuccessor(vectorS)
    print(localCon.generateSuccessor(vectorS))

    print(problem.getSuccessors(localCon.getPosition()))

    print(localCon.getPosition())
    
    actions.append(s)
    actions.append(s)
    actions.append(w)
    """

    # maybe will not need to track visited coordinates becuase of using stack for DFS

    # return  [s, s, w, s, w, w, s, w]
    
    """Pseudocode
    function graphSearch saerch()
        closed <- an empty set (visited)
        fringe <- INSERT(MAKE-NODE(INITIAL-STATE[problem],fringe))
        loop do
            if fringe is empty then return failure 
            node <-REMOVE-FRONT(fringe)
            if GOAL-TEST(problem,STATE[node])then return node
            if STATE[node] is not in closed then 
                add STATE[node] to closed 
                for child in EXPAND(state[node], problem) do
                    fringe.insert(childnode,fringe)
    /pseudocode
    """
    visited = []
    startState = problem.getStartState() 
    localCon = Configuration(startState, None) #effectively node later...
    firstTime = True

    fringe.push(localCon)
    import time


    #history handling vars
    pastNode = localCon
    #position = None
    x = 0
    y = 0


    while not fringe.isEmpty():
        time.sleep(1)
        node = fringe.pop() #list [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
        if not firstTime:
            actions.append(node)
            print(node.getDirection())
        firstTime = False
        if problem.isGoalState(node.getPosition()):
            # print(actions)
            for item in actions:
                print(item.getPosition(), " and go ", item.getDirection()) 
            return actions 
        # print(node.getPosition())
        if  node.getPosition() not in visited: #(visited.__contains__(localCon.getPosition())
            print(node.getPosition())
            visited.append(node.getPosition())
            # get options   
            options = problem.getSuccessors(node.getPosition())
            for coor,dir,cost in options:
                #work
                node = Configuration(coor,dir)
                fringe.push(node)
        
        #history handling (path reporting help)
        position = pastNode.getPosition()
        x = position[0]
        y = position[1]

        position = node.getPosition()
        curX = position[0]
        curY = position[1]
        
        tempNode = Configuration((1,1),'North')

        if(abs(curX - x) > 1 | abs(curY - y) > 1):
            #always illegal move, need to cut history
            print("No teleporting")
            node = fringe.pop()
            pruneHistory(node,tempNode,actions)

        if(abs(curX - x) == 1 & abs(curY - y) == 1):
            #always illegal move, need to cut history
            print("No teleporting")
            node = fringe.pop()
            pruneHistory(node,tempNode, actions)


        # if(pastNode.getPosition()):
        #     print("nope")
            #end if
        pastNode = node
        #end while


    # for item in actions:
    #     print(item.getPosition(), " and go ", item.getDirection()) 


    return actions


    # problem.applyAction(problem.getStartState(), problem.getAction())

    """
    Plan:
    1) Figure out how to move at all (applyaction?)
        - Determine what exactly action and movement vector are??
    2) Look into the stack implentation in util
    3) Code the DFS implementations
    
    """

    #return actions 
    util.raiseNotDefined()



def pruneHistory(node, tempNode, actions):
    # pop off items until item removed is equal to node, then push it back on
    from game import Configuration
    print("pruneHistory node ", node.getPosition())
    print("pruneHistory tempNode ", tempNode.getPosition())

    tempNode = actions.pop()    
    print("HERE")

    # nodePos = node.getPosition()
    # tempNodePos = tempNode.getPosition()
    

    while tempNode.getPosition() != node.getPosition():
        print("in while")
        print("tempNode is ", tempNode.getPosition())
        tempNode = actions.pop()

    actions.append(tempNode)

    print("not implemented pruneHistory yet")
    #end pruneHistory

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
