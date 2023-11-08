#adding 2 np.array([]) yields adding each position and summing that same position

#input

#we store each coord in the set

#To find the covered, we check the neighbor of each of the faces e.g. set 2 numpy arrays to + 1 and -1 of each position and add them and check if they are in filled and we are 
#doing this for 0, 1, 2 which denotes the index of the set, and then we check if that neighbor which for ex. on the trace is 0 currently and it looks like this (1, 0, 0) if it is 
#and the pos is (2,3,4) it checks (3, 3, 4) for that neigbor and if it exists then it adds 1 to the covered and you do that for all of the coords of each point and all their 
#adjacent faces

#Then for each cube coord we subdract covered from 6 to get the answer.

#should add 1 to covered if true since true denotes 1?
#covered += tuple(np.arr([]) + np.arr([])) in filled
import numpy as np
covered = 0
filled = set()
filled.add((2,3,4))
covered += tuple(np.array([1,1,2]) + np.array([1, 2, 2])) in filled
print(covered)