#contents is basically a 2d array already
with open('input/day8.in') as file:
    contents = [i.strip() for i in file.readlines()]

rows, cols = (len(contents), len(contents[0]))
count = 0
t = [[0] * cols for _ in range(rows)]
#need to load it in a 2d array b/c we only have access to one line at a time and we need to compare multiple rows and cols
for i in range(rows):
    for j in range(cols):
        t[i][j] = int(contents[i][j])

#outside edges
count += (2 * rows) + (2 * cols)
leftvisible = True
rightvisible = True
upvisible = True
downvisible = True

#inside edges
for i in range(1, rows-1):
    for j in range(1, cols-1):
        up = i - 1
        down = i + 1 
        left = j - 1
        right = j + 1
        while left != 0:
            #if the left is greater at any point just break, the curr tree can't be seen
            #separate the case that it ends and it encounters a tree that's blocking the curr one
            if t[i][j] <= t[i][left]:
                leftvisible = False
            left -= 1
        while right != cols-1:
            if t[i][j] <= t[i][right]:
                rightvisible = False
            right += 1
        while up != 0:
            if t[i][j] <= t[up][j]:
                upvisible = False
            up -= 1 
        while down != rows-1:
            if t[i][j] <= t[down][j]:
                downvisible = False
            down += 1
        if leftvisible or rightvisible or downvisible or upvisible:
            count += 1
print('count', count)
        
#When it breaks does it go to the top for loop or does it go to the loop under it?