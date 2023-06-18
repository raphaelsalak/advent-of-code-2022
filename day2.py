with open('day2input.txt') as file:
    lines = []
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    prioritySum=0
    for line in file:
        lines.append(line.rstrip())
    for line in lines:
        for a in range(0, len(line)//2): #this needs to traverse the 
            for b in range(len(line)//2+1, len(line)):
               if line[a] == line [b]:
                for index, entry in enumerate(letters):
                   if entry == line[a]:
                      prioritySum += index + 1
    print(prioritySum)
                      
                   

                