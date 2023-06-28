#contents is basically a 2d array already
with open('input/day8.in') as file:
    contents = [i.strip() for i in file.readlines()]

rows, cols = (len(contents), len(contents[0]))
count = 0
t = [[0] * cols for _ in range(rows)]
#need to load it in a 2d array b/c we only have access to one line at a time and we need to compare multiple rows and cols
for i in range(rows):
    for j in range(cols):
        t[i][j] = contents[i][j]

#outside edges
count += (2 * rows) + (2 * cols)

#inside edges

print('count so far', count)