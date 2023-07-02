
with open('input/day8.in') as file:
     data = [row.strip() for row in file.readlines()]
ROWS = len(data)
COLUMNS = len(data[0])
#There's overlap in rows and columns so columns - 2 to get rid of the ones ROWS already has
edges = (ROWS * 2) + ((COLUMNS-2)*2)
total = edges
for row in range(1, ROWS -1):
    for col in range(1, COLUMNS-1):
        tree = data[row][col]
        right = [data[row][col-i] for i in range(1, col+1)]
        left = [data[row][col+i] for i in range(1, COLUMNS-col)]
        up = [data[row-i][col] for i in range(1, row+1)]
        down = [data[row+i][col-i] for i in range(1, ROWS-row)]

        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            total += 1
print('count', total)