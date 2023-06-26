# <= 100,000 and sum of those products
# object file with name, size attribute
class custom_file:
    def __init__(self, name, size, dir):
        self.name = name
        self.size = size
        self.dir = dir
# dictionaries mapped to files or other dictionaries or files
# {a:{file}, b:file}
# {a:{file, b:{file}, c:{file}} 

# read in input and make the data structures simultaneously
with open('input/input7.txt') as file:
    contents=file.read().splitlines()
for i in contents:
    command_list = i.split()
    #process command name and corresponding command arg
    '''
    loading in the data structure
    if cd x
        if it exists
            go to it
    else if cd .. 
        if pwd != c / 
            go back words
    else if ls
    else if dir x
        mkdir x
    else
        make a file in the current list
        self.name = firstarg
        self.size = secondarg
    '''
    '''
    traversing to find size file size of each directory <= 100,000 and summing all of them
    QS how to keep track of each directories and their respective sizes?
    ANS when the recursion back tracks, if the size of the directory's children is <= 100,000 add to total sum. Print out the sum. 
    is more of a graph than a tree

    if currnode has children
        go into them
    else if is a file
        add the size to a recursive call that back track stops at the dir and some how compares it to <= 100,000 and if true adds it to the total sum of the graph.
    '''
    print(command_list)
print(command_list)

    

# traverse each directory and find which directories including their subdirectories have <= 100,000 size
# Then print sum all the sizes
with open("input/input7.txt") as file:
    commands = [command.strip() for command in file.readlines()]
path = "/home"
dirs = {"/home":0}

#process every command
for command in commands:
    #commands that start with the $
    if command[0] == "$":
        #do nothing when listing directories or files
        if command[2:4] == "ls":
            pass
    # Manage changing paths
    elif command[2:4] == "cd":
        # go back to root
        if command[5:6] == "/":
            path = "/home"
        #go back in the path
        elif command[5:7] == "..":
            #gives the last occurence of /
            path = path[:path.rfind("/")]
        #change path
        else:
            dir_name = command[5:]
            path = path + "/" + dir_name
            dirs.update(path{:0})
    elif command[0:3] == "dir":
        pass
    else:
        size = int(command[:command.find(" ")]) #get the size of the file
        dir = path
        #start backtracking back and adding the file sizes all the way to home
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]
    #get the file size and change directories in which it was found
total = 0

for dir in dirs:
    if dirs[dir] <= 100000:
        total += dirs[dir]
print("answer to part 1: ", total)

    