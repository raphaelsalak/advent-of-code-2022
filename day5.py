# Open the file
with open('input5.txt', 'r') as file:
    #strip the last \n so you can split the stack strings and instructions
    stack_strings, instructions = (line.splitlines() for line in file.read().strip("\n").split("\n\n"))
print(instructions)
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]

def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")
def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
                stack_num += 1
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

loadStacks()
displayStacks()
emptyStacks()
displayStacks()