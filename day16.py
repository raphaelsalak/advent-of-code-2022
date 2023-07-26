with open('input/day16.in') as file:
    contents = file.read().strip().split('\n')
print(contents)
#the math is how ever long it's active in the 30 minutes * flow rate and then take the sum of all of them
#extract the flow rate and nodes and their neigbors from input
for i in contents:
    line = i.split(' ')
    node = line[1]
    rate = line[4]
    neighbors = line[9:]
    print(neighbors)

    
#dfs recursive with flow rate labled as 'rate' and accessed like that
#in dfs determine if your gonna open the current valve or move to the next valve
#30 iterations
#the logic goes like this, is it better to stay at the current node to turn the valve or is it better to go to the next neighbor to increase pressure
#keep track of the pressure and keep cummulating each iteration based on the logic.
#at the end print the answer