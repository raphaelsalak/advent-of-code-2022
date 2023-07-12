#x =1 on noop
#after the third cycle x=4
#we execute based on the cycle and the num
with open('input/day10.in') as file:
    contents = [i.strip().split() for i in file.readlines()]
sum = 1
cycle = 1
#iterate through the whole thing
for line in contents:
    cycle += 1
    if len(line) == 2:
        amount = abs(int(line[1]))
    else:
        cycle += 1
    if amount < cycle:
        continue
    while cycle < amount:
        cycle += 1
        if cycle == 20:
            sum *= 20 
        elif cycle == 60:
            sum *= 40
        elif cycle == 100:
            sum *= 100
        elif cycle == 140:
            sum *= 140
        elif cycle == 180:
            sum *= 180
        elif cycle == 220:
            sum *= 220
    sum += amount
print('sum', sum)
        
    
#for each line check if the number is equal to cycle and if it is, execute it



print(contents)
