#contents is basically a 2d array already
with open('input/day8.in') as file:
    contents = [i.strip() for i in file.readlines()]

rows, cols = (len(contents), len(contents[0]))
count = 0
t = [[0] * cols for _ in range(rows)]
#need to load it in a 2d array b/c we only have access to one line at a time and we need to compare multiple rows and cols

#outside edges
count += (2 * rows) + (2 * cols)

#inside edges
for i in range(1, rows):
    for j in range(1, cols):
        up = i - 1
        down = i + 1 
        left = j - 1
        right = j + 1
        while left != -1:
            #if the left is greater at any point just break, the curr tree can't be seen
            if t[i][j] <= t[i][left]:
                break
            left -= 1
        count += 1
        while right != cols:
            if t[i][j] <= t[i][right]:
                break
            right += 1
        count += 1
        while up != -1:
            if t[i][j] <= t[up][j]:
                break
            up -= 1 
        count += 1
        while down != rows:
            if t[i][j] <= t[down][j]:
                break
            down += 1
        count += 1
print('count', count)
#When it breaks does it go to the top for loop or does it go to the loop under it?