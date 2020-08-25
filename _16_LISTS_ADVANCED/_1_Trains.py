wagons_n = int(input())
train = [0] * wagons_n
while True:
    command = input().split()
    if command[0] == 'End':
        break

    if command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        train[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        # if int(command[2])<=train[int(command[1]):
        train[int(command[1])] -= int(command[2])
        # else:
        #     print('Ignore this nonsense.')
print(train)
