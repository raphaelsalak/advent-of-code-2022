def appendLevel(alist, level, something):
    if level == 1:
        alist.append(something)
    elif level == 2:
        print(alist)
        alist[0].append(something)
    elif level == 3:
        alist[0][0].append(something)
    elif level == 4:
        alist[0][0][0].append(something)

def length(somestring):
    i = 0
    count = 0
    maxcount = 0
    a = []
    while len(somestring) > 0 and i <= len(somestring) - 1:
        if somestring[i] == '[':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 0
        i += 1
    return maxcount
with open('input/day13.in') as file:
    contents = file.read().strip().split('\n\n')
#comparing int vs int, list vs list, int vs list, list vs int
#need to somehow parse each line string and convert it to a list? or parse and solve using the string '[]' ?
#how to convert string input to list
a = []
level = 0
ignore = [']', ',', '[']
for i in contents:
    first, second = i.split('\n')
    #maxlength = length(first)
    for c in first:
        if c == '[':
            appendLevel(a, level, [])
            level += 1
        elif c not in ignore:
                level -= 1
                #read in comma to get the whole number e.g. 1 to 10.
                num = int(c)
                appendLevel(a, level, num)
                #append num to the current level
print(a)

    #

            
                

            



        


