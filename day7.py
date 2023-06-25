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
    print(command_list)
print(command_list)

    

# traverse each directory and find which directories including their subdirectories have <= 100,000 size
# Then print sum all the sizes
