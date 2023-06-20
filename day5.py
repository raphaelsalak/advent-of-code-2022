import re
# Open the file
with open('input/input5.txt', 'r') as file:
    #strip the last \n so you can split the stack strings and instructions
    stack_strings, instructions = (line.splitlines() for line in file.read().strip("\n").split("\n\n"))
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}
#index then the content ex. 1, bob
#by getting the index of the chars in the last line, we can find where the crates belong to.
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]
print("first one", indexes)
print("chars", )


def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")
def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        print(string)
        for index in indexes:
            #this only looks at the letters which are lined up with the indexes of the numbers we found earlier.
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

loadStacks()
displayStacks()
print(instructions)
for instruction in instructions:
    instruction_list = instruction.split()
    quantity = int(instruction_list[1])
    from_list = int(instruction_list[3])
    to_list = int(instruction_list[5])
    #cut a list slice from the old one
    list_slice = stacks[from_list][-quantity:]
    list_slice = list_slice[::-1]
    #append that list to the to list
    for i in list_slice:
        stacks[to_list].append(i)
    #delete that old list
    #stacks[from_list] = stacks[from_list][-quantity::-1]
    stacks[from_list] = stacks[from_list][:-quantity:]
displayStacks()

    
    

