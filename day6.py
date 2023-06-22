with open('input/input6.txt') as file:
    contents = file.read().strip()

#parse the whole thing character by character
inc = 1
counter = 0
string = contents[0]
print(contents)
for i, char in enumerate(contents):
    start = i+1
    end = i+5
    for j in range(start, end):
    #store the characters 4 at a time
    #stores the first character fine
        #if j doesn't equal i
        #add that to the string
        if contents[j] != char:
            string += contents[j]
            inc += 1
            if inc == 4:
                counter = end
                break
        else:
            inc = 0
print('index', counter + 1)
    # , as you store them 
    # check if the incoming character is in the string. 
    # if it is, restart the 4 increment. 
    # if it's not keep going until you hit 4 and update the counter