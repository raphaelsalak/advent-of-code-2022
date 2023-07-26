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
#comparing int vs int, list vs list, int vs list, list vs int #need to somehow parse each line string and convert it to a list? or parse and solve using the string '[]' ?
#use eval
#a = [b]
#isinstance()
#if the preprocessing is too hard, then there must be an easier built in way to do it e.g. eval an isintance() so if you think the processing is too hard start doing research or look at hints in the solution