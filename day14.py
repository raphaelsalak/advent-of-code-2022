with open('input/day15.in') as file:
    contents = [i.split(':') for i in file.read().strip().split('\n')]


def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
not_beacons = set()

for i, arg in enumerate(contents):
    for j in range(len(arg)):
        contents[i][j] = contents[i][j].split(',')
       # index = contents[i][j].find('=') + 1
       # contents[i][j] = contents[i][j][index::]
for i, arg in enumerate(contents):
    for j, arg2 in enumerate(arg):
        for k, arg3 in enumerate(arg2):
            index = contents[i][j][k].find('=') + 1
            contents[i][j][k] = int(contents[i][j][k][index:])
for i in contents:
    for j in i:
        not_beacons.add(tuple(j))
print(not_beacons)


