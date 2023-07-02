with open('input/day9.in') as file:
    contents = [i.strip().split() for i in file.readlines()]
print(contents)
#keep a sum of the total steps
total=0
#keep track of opposites
for i in range(0, len(contents)-1):
    if contents[i][0] == 'L' and contents[i+1][0] == 'R':
        total += abs(int(contents[i+1][1]) - int(contents[i][1]) + 1)
    elif contents[i][0] == 'R' and contents[i+1][0] == 'L':
        total += abs(int(contents[i+1][1]) - int(contents[i][1]) + 1)
    elif contents[i][0] == 'U' and contents[i+1][0] == 'D':
        total += abs(int(contents[i+1][1]) - int(contents[i][1]) + 1)
    elif contents[i][0] == 'D' and contents[i+1][0] == 'U':
        total += abs(int(contents[i+1][1]) - int(contents[i][1]) + 1)
    else:
        total += int(contents[i][1])
last = contents[-1][0]
before = contents[-2][0]
if last == 'L' and before == 'R':
    total += abs(int(contents[-1][1]) - int(contents[-2][1]) + 1)
elif last == 'R' and before == 'L':
    total += abs(int(contents[-1][1]) - int(contents[-2][1]) + 1)
elif last == 'U' and before == 'D':
    total += abs(int(contents[-1][1]) - int(contents[-2][1]) + 1)
elif last == 'D' and before == 'U':
    total += abs(int(contents[-1][1]) - int(contents[-2][1]) + 1)
else:
    total += int(contents[-1][1])

print('count', total)


