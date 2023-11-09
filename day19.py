#Fastest way to get geode robots

#For each blue print run a 24 min scenario.
#store each robot in a dict?

#input
#dfs
with open('input/day19.in') as file:
    content = file.readlines()
    lines = [line.strip() for line in content]

print(lines)

robots = {'orerobot':[1, 0, 0], 'clayrobot':[0,0,0], 'obsidianrobot': [0,0,0], 'geoderobot' : [0,0,0]}

for line in lines:
    for i in range(1, 25):
        pass