with open('input/input6.txt') as file:
    contents = file.read().strip()

#parse the whole thing character by character
inc = 0
counter = 0
string = contents[0] 
for i in range(1, len(contents)):
    #store the characters 4 at a time
    if contents[i] not in string:
        string += contents[i]
        inc += 1
        if inc == 3:
            counter += 1
            inc = 0
print('Occurences: ', counter)


    # , as you store them 
    # check if the incoming character is in the string. 
    # if it is, restart the 4 increment. 
    # if it's not keep going until you hit 4 and update the counter