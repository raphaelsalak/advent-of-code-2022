import numpy as np
#read input
with open('input/day17.in') as file:
    content = file.read().rstrip('\n')
    print(content)
    for c in content:
        pass
        
alphabet = {'first' : ((2,0), (3,0), (4,0), (5,0))}
#initialize set
covered = 0
points = set()
points.add((3,4,5))
covered += tuple((2,3,4) + (1,1,1)) in points
points.add((2, 3, 4))
points.add((1, 1, 1))
first = np.array([1,1,1])
second = np.array([2,3,4])
print(tuple(first + second))


print(covered)