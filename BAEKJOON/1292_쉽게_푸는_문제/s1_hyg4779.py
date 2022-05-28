from collections import deque

N, M = map(int, input().split())


arr = [0]
for i in range(1, M+1):
    for j in range(i):
        arr.append(i)

result = 0

for v in range(N, M+1):
    result += arr[v]

print(result)