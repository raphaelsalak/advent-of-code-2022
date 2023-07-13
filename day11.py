with open('input/day11.in') as file:
    blocks = [line.split('\n') for line in file.read().strip().split('\n\n')]
#store all the monkeys and their rules
for line in blocks:
    print(line[0])
    line[0] = line[0].replace('Monkey ', '').strip()
    line[0] = line[0].replace(':', '').strip()
    line[1] = line[1].replace('Starting items: ', '').strip()
    line[1] = line[1].replace(' ', '').strip()
    line[2] = line[2].replace('Operation: new = old ', '').strip()
    line[3] = line[3].replace('Test: divisible by ', '').strip()
    line[4] = line[4].replace('If true: throw to monkey ', '').strip()
    line[5] = line[5].replace('If false: throw to monkey ', '').strip()
for i in blocks:
    i[0] = int(i[0])
    i[1] = i[1].split(',')
    i[1] = [int(num.strip()) for num in i[1]]
    i[2] = i[2].split()
    i[3] = int(i[3])
    i[4] = int(i[4])
    i[5] = int(i[5])
    
#run a while loop to simulate 20 rounds
new = 0
value = ''
inspect = [0,0,0,0,0,0,0,0]

for _ in range(0,20):
    for i, monkey in enumerate(blocks):
        operation = monkey[2][0]
        div = monkey[3]
        first = monkey[4]
        second = monkey[5]
        for j in monkey[1]:
            if len(monkey[1]) != 0:
                inspect[i] += len(monkey[1]) 
                if value == 'old':
                    value = j
                else:
                    value = int(j)
                if operation == '*':
                    new = j * value
                elif operation == '+':
                    new = j + value
                if new % div == 0:
                    #true
                    blocks[first][1].append(j)
                    blocks[i][1].remove(j)
                    #remove 
                else:
                    #false
                    blocks[second][1].append(j)
                    blocks[i][1].remove(j)
    #run through all the items for each monkey
most = max(inspect)
firstmost = most
inspect.remove(most)
most = max(inspect)
secondmost = most
print('the answer is ', firstmost * secondmost)


