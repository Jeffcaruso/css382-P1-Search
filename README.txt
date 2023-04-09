Project 1

Jeffrey Caruso, Daniela Cuevas

Q1
DFS, tried to use puseudo code for graph search in Lecture slides to get us started.

Q2
BFS, tried to use puseudo code for graph search in Lecture slides to get us started.
As DFS had the same graph search alogirthm, we ended up only having to change the fringe 
to be queue instead of a stack. 

Q3
UCS, tried to use puseudo code for graph search in Lecture slides to get us started.
As BFS has the same basic details, we started with BFS, 
then added the code to make the costs be filled in.

Q4
A*, started with UCS. Added heuristic to prioritization for PriorityQueue

Q5
Used the existing get successors for inspiration, and ideas on what we actually need to return. 
We are using the state[0] for the actual current state. state[1] for the visited locations (corners).

Q6
Used ManhattanDistance to find shortest route to a non visited corner.
Then 'navigated' (teleported) to that location, found the next corner. Continued until done.
So at the beginning, the heuristic was much longer than just getting to the first corner position.

Q7
Used ManhattanDistance. Found ManhattanDistance for the shortest distance, 
Found ManhattanDistance for the longest distance; Calculations of:
heuristic = closestDistance + ManhattanDistance(shortestDitanceNode, longestDistanceNode)

Q8
Largely was finishing goal state. 
For goal state, we checked if the given state was on a food item. 
For AnyFoodSearchProblem, we used UCS of the problem.

Summary:
Overall, based on autograder, 25/25.


