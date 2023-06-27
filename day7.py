with open("input/day7.in.txt") as file:
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
                dirs.update({path:0})
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
total = 70000000
#find the path that is the least but frees up >= 8,381,165
a = []
total_unused_space = total - dirs['/home']
print('you need to free this much ', 30000000 - total_unused_space)
for dir in dirs:
    if dirs[dir] >= 208860:
        a.append(dirs[dir])
a.sort()
print(a[0])
