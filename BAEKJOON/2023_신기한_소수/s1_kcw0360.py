import math


N = int(input())
numbers = ['1', '2', '3', '5', '7', '9']
answer = []

def find(x):
    for i in numbers:
        flag = True
        temp = x + i
        if len(temp) == 1:
            if temp == '1' or temp == '9':
                continue
        else:
            for j in range(2, int(math.sqrt(int(temp)))+1):
                if int(temp) % j == 0:
                    flag = False
                    break

        if flag:
            if len(temp) == N:
                answer.append('{}\n'.format(temp))
            else:
                find(temp)

find('')

print(''.join(answer))