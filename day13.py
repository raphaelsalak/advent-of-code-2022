with open('input/day13.in') as file:
    contents = file.read().strip().split('\n\n')
#comparing int vs int, list vs list, int vs list, list vs int
#need to somehow parse each line string and convert it to a list? or parse and solve using the string '[]' ?
#how to convert string input to list

def length(somestring):
    i = 0
    count = 0
    maxcount = 0
    while len(somestring) > 0 and i <= len(somestring) - 1:
        if somestring[i] == '[':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 0
        i += 1
    return maxcount
for i in contents:
    first, second = i.split('\n')
    maxlength = length(first)
    print(maxlength)

