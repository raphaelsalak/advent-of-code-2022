with open('input/input6.txt') as file:
    contents = file.read().strip()

#parse the whole thing character by character
print(contents)
for i in range(4, len(contents)):
    #given an iterable, will return a new non duplicate iterable, could change length of for ex. a list 
    s = set(contents[(i-4):i])
    print(s)
    if len(s) == 4:
        print('total', i)
        break
    # , as you store them 
    # check if the incoming character is in the string. 
    # if it is, restart the 4 increment. 
    # if it's not keep going until you hit 4 and update the counter