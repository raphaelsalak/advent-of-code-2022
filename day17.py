#read input
with open('input/day17.in') as file:
    content = file.read().rstrip('\n')
    print(content)
    for c in content:
        pass
        
alphabet = {'first' : ((2,0), (3,0), (4,0), (5,0))}
#initialize set
points = set()
points.add(alphabet.get('first'))
points.add((0, 0))
points.add((2, 0))
points.add((0, 2))
points.add((2, 2))

print(points)